from __future__ import annotations

import ast
import sys


class Visitor(ast.NodeVisitor):
    def __init__(self):
        self._in_async_def = False

    def visit_FunctionDef(self, node):
        self._in_async_def, orig = False, self._in_async_def
        self.generic_visit(node)
        self._in_async_def = orig

    def visit_AsyncFunctionDef(self, node):
        self._in_async_def, orig = True, self._in_async_def
        self.generic_visit(node)
        self._in_async_def = orig

    def visit_For(self, node):
        print(f'got `for` on line {node.lineno} | {self._in_async_def}')
        self.generic_visit(node)


def main():
    with open(sys.argv[1], 'rb') as f:
        Visitor().visit(ast.parse(f.read(), filename=sys.argv[1]))


if __name__ == '__main__':
    raise SystemExit(main())
