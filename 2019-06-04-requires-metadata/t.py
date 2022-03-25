from __future__ import annotations

import argparse
import contextlib
import os.path
import subprocess
import sys
import tempfile

import importlib_metadata


@contextlib.contextmanager
def onpath(whl):
    before = sys.path[:]
    try:
        sys.path.insert(0, whl)
        yield
    finally:
        sys.path[:] = before


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('pkg')
    parser.add_argument('--include-extras', action='store_true')
    args = parser.parse_args()

    pkgname, *_ = args.pkg.partition('==')

    with tempfile.TemporaryDirectory() as tmp:
        cmd = ('pip', 'wheel', '--no-deps', args.pkg, '-w', tmp)
        subprocess.check_call(cmd, stdout=subprocess.DEVNULL)
        filename, = os.listdir(tmp)
        filename = os.path.join(tmp, filename)

        with onpath(filename):
            print('*' * 79)
            print(f'{args.pkg}:')
            dist = importlib_metadata.distribution(pkgname)
            for req in dist.metadata.get_all('requires-dist'):
                if not args.include_extras and 'extra == ' in req:
                    continue
                print(f'- {req}')


if __name__ == '__main__':
    raise SystemExit(main())
