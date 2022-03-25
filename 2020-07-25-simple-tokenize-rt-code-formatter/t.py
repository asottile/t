from __future__ import annotations

import argparse
import ast
import sys
import tokenize
import warnings
from typing import Sequence

from tokenize_rt import ESCAPED_NL
from tokenize_rt import Offset
from tokenize_rt import reversed_enumerate
from tokenize_rt import src_to_tokens
from tokenize_rt import tokens_to_src
from tokenize_rt import UNIMPORTANT_WS

NEWLINES = frozenset((ESCAPED_NL, 'NEWLINE', 'NL'))
INDENT_TOKENS = frozenset(('INDENT', UNIMPORTANT_WS))


REWRITABLE_TYPES = (
    ast.Dict,
    ast.List,
    ast.Set,
    ast.Tuple,
    # TODO: comprehension types as well
)


def ast_parse(contents_text: str) -> ast.Module:
    # intentionally ignore warnings, we might be fixing warning-ridden syntax
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        return ast.parse(contents_text.encode())


class Visitor(ast.NodeVisitor):
    def __init__(self) -> None:
        self.calls: set[Offset] = set()

    def visit_Call(self, node: ast.Call) -> None:
        if (
                not node.keywords and
                len(node.args) == 1 and
                isinstance(node.args[0], REWRITABLE_TYPES) and
                node.args[0].lineno == node.lineno + 1
        ):
            self.calls.add(Offset(node.lineno, node.col_offset))

        self.generic_visit(node)


def _fix_calls(contents_text: str) -> str:
    try:
        ast_obj = ast_parse(contents_text)
    except SyntaxError:
        return contents_text

    visitor = Visitor()
    visitor.visit(ast_obj)

    if not visitor.calls:
        return contents_text

    try:
        tokens = src_to_tokens(contents_text)
    except tokenize.TokenError:  # pragma: no cover (bpo-2180)
        return contents_text

    for i, token in reversed_enumerate(tokens):
        if token.offset in visitor.calls:
            visitor.calls.discard(token.offset)

            # search forward for the opening brace
            while tokens[i].src != '(':
                i += 1

            call_start = i
            i += 1
            brace_depth = 1
            start = -1
            end = -1

            while brace_depth:
                if tokens[i].src in {'(', '{', '['}:
                    if brace_depth == 1:
                        start = i
                    brace_depth += 1
                elif tokens[i].src in {')', '}', ']'}:
                    brace_depth -= 1
                    if brace_depth == 1:
                        end = i
                i += 1

            assert start != -1
            assert end != -1
            call_end = i - 1

            # dedent everything inside the brackets
            for i in range(call_start, call_end):
                if (
                        tokens[i - 1].name == 'NL' and
                        tokens[i].name == UNIMPORTANT_WS
                ):
                    tokens[i] = tokens[i]._replace(src=tokens[i].src[4:])

            del tokens[end + 1:call_end]
            del tokens[call_start + 1:start]

    return tokens_to_src(tokens)


def _fix_file(filename: str) -> int:
    if filename == '-':
        contents_bytes = sys.stdin.buffer.read()
    else:
        with open(filename, 'rb') as fb:
            contents_bytes = fb.read()

    try:
        contents_text_orig = contents_text = contents_bytes.decode()
    except UnicodeDecodeError:
        print(f'{filename} is non-utf-8 (not supported)')
        return 1

    contents_text = _fix_calls(contents_text)

    if filename == '-':
        print(contents_text, end='')
    elif contents_text != contents_text_orig:
        print(f'Rewriting {filename}', file=sys.stderr)
        with open(filename, 'w', encoding='UTF-8', newline='') as f:
            f.write(contents_text)

    return contents_text != contents_text_orig


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*')
    args = parser.parse_args(argv)

    retv = 0
    for filename in args.filenames:
        retv |= _fix_file(filename)

    return 1


if __name__ == '__main__':
    raise SystemExit(main())
