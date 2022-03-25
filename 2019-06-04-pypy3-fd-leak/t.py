from __future__ import annotations

import warnings

import pytest


def test():
    for _ in range(15000):
        with pytest.raises(IsADirectoryError):
            with open('.'):
                pass


with warnings.catch_warnings(record=True) as wrns:
    warnings.simplefilter('always')
    test()


if len(wrns):
    print('*' * 79)
    print(f'warnings: {len(wrns)}')
    print('first warning:')
    print(f'{wrns[0].filename}:{wrns[0].lineno}:{wrns[0].message}')
    print('*' * 79)
