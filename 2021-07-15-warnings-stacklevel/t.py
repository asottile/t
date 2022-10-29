import ast
import collections
import json
import sys


class Visitor(ast.NodeVisitor):
    def __init__(self) -> None:
        self.levels = collections.defaultdict(int)
        self.unparseable = 0
        self.default = 0

    def visit_Call(self, node: ast.Call) -> None:
        if (
            isinstance(node.func, ast.Attribute) and
            node.func.attr == 'warn' and
            isinstance(node.func.value, ast.Name) and
            node.func.value.id == 'warnings'
        ):
            for keyword in node.keywords:
                if keyword.arg == 'stacklevel':
                    if isinstance(keyword.value, ast.Num):
                        self.levels[keyword.value.n] += 1
                    else:
                        self.unparseable += 1
                    break
            else:
                self.default += 1


def main() -> int:
    visitor = Visitor()
    for filename in sys.argv[1:]:
        with open(filename, 'rb') as f:
            try:
                visitor.visit(ast.parse(f.read(), filename=filename))
            except SyntaxError:
                print(f'SyntaxError: {filename}')

    print(json.dumps(visitor.levels, indent=2))
    print(f'unparseable: {visitor.unparseable}')
    print(f'default: {visitor.default}')


if __name__ == '__main__':
    raise SystemExit(main())
