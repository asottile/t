import ast
import collections
import pprint
import sys


class V(ast.NodeVisitor):
    def __init__(self):
        self.name_to_type = collections.Counter()

    def visit_FunctionDef(self, node):
        args = node.args.posonlyargs + node.args.args + node.args.kwonlyargs
        for arg in args:
            if arg.annotation:
                self.name_to_type[(arg.arg, ast.unparse(arg.annotation))] += 1
        if node.args.vararg and node.args.vararg.annotation:
            k = (
                f'*{node.args.vararg.arg}',
                ast.unparse(node.args.vararg.annotation),
            )
            self.name_to_type[k] += 1
        if node.args.kwarg and node.args.kwarg.annotation:
            k = (
                f'**{node.args.kwarg.arg}',
                ast.unparse(node.args.kwarg.annotation),
            )
            self.name_to_type[k] += 1
        self.generic_visit(node)

    visit_AsyncFunctionDef = visit_FunctionDef

    def visit_AnnAssign(self, node):
        if isinstance(node.target, ast.Name):
            name = node.target.id
        elif isinstance(node.target, ast.Attribute):
            name = node.target.attr
        else:
            raise NotImplementedError(node.target)
        self.name_to_type[(name, ast.unparse(node.annotation))] += 1
        self.generic_visit(node)


def main() -> int:
    v = V()
    for filename in sys.argv[1:]:
        with open(filename, 'rb') as f:
            contents = f.read()
        v.visit(ast.parse(contents, filename=filename))

    pprint.pprint(v.name_to_type.most_common(20))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
