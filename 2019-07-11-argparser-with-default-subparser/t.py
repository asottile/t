from __future__ import annotations

import argparse
import collections


class AlwaysContains(collections.defaultdict):
    def __contains__(self, _):
        return True


class WildSubParsersAction(argparse._SubParsersAction):
    def __init__(self, *args, **kwargs):
        all_args_parser = argparse.ArgumentParser()
        all_args_parser.add_argument('arg', nargs='*')
        self.__name_parser_map = AlwaysContains(lambda: all_args_parser)
        super().__init__(*args, **kwargs)

    @property
    def _name_parser_map(self):
        return self.__name_parser_map

    @_name_parser_map.setter
    def _name_parser_map(self, _):
        pass  # intentionally ignore assignments


class WildArgumentParser(argparse.ArgumentParser):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.register('action', 'parsers', WildSubParsersAction)


def main():
    parser = WildArgumentParser()
    subparsers = parser.add_subparsers(dest='parser')
    subparsers.required = True
    foo_parser = subparsers.add_parser('foo')
    foo_parser.add_argument('wat')
    args = parser.parse_args()

    if args.parser == 'foo':
        print(f'do foo {args.wat}')
    else:
        print(f'passthrough: {args.parser} {args.arg}')


if __name__ == '__main__':
    raise SystemExit(main())
