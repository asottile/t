from __future__ import annotations

import functools
import itertools
import os.path
import subprocess
import sys
import time
from typing import NamedTuple

N = 100
REPOS = (('reorder_python_imports', 'v3.1.0'), ('classify-imports', 'v3.0.2'))


class Version(NamedTuple):
    ts: int
    repo: str
    rev: str

    @classmethod
    def parse(cls, repo: str, s: str) -> Version:
        ts, rev = s.split()
        return cls(int(ts), repo, rev)


def ts_repo_rev(repo: str, rev: str) -> list[Version]:
    out = subprocess.check_output((
        'git', '-C', repo, 'log', '--first-parent', '--format=%ct %h',
        f'{rev}^..origin/HEAD',
    ))
    return [Version.parse(repo, line) for line in out.decode().splitlines()]


def _do_install(repo: str, rev: str) -> None:
    repo = os.path.abspath(repo)
    subprocess.check_call(('git', '-C', repo, 'checkout', '-q', rev))
    cmd = ('pre-commit/venv/bin/pip', 'install', '-q', '--no-deps', repo)
    subprocess.check_call(cmd)


def _best(cmd: tuple[str, ...]):
    best: float = sys.maxsize
    for _ in range(N):
        t0 = time.monotonic()
        subprocess.call(cmd, cwd='pre-commit')
        t1 = time.monotonic()
        best = min(best, t1 - t0)
    return best


@functools.lru_cache(maxsize=1)
def _py_files() -> tuple[str, ...]:
    cmd = ('git', '-C', 'pre-commit', 'ls-files', '--', '*.py')
    out = subprocess.check_output(cmd)
    return tuple(line for line in out.decode().splitlines())


def main() -> int:
    revs = {k: ts_repo_rev(k, v) for k, v in REPOS}
    versions = sorted(itertools.chain.from_iterable(revs.values()))

    cur = {k: v[-1].rev for k, v in revs.items()}
    for k, v in cur.items():
        _do_install(k, v)

    for ts, repo, rev in versions:
        if cur[repo] == rev:
            continue

        _do_install(repo, rev)
        cur[repo] = rev

        print(ts, *cur.values(), sep='\t', end='', flush=True)
        for cmd in (
                ('venv/bin/python', '-c', 'import reorder_python_imports'),
                ('venv/bin/reorder-python-imports', *_py_files()),
                ('venv/bin/reorder-python-imports', '--py310', *_py_files()),
        ):
            print(f'\t{_best(cmd):.5f}', end='', flush=True)
        print(flush=True)

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
