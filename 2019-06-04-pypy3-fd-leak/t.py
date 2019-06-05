import io
import warnings

import pytest


def test():
    for _ in range(15000):
        with pytest.raises(IsADirectoryError):
            with io.open('.'):
                pass


with warnings.catch_warnings(record=True) as wrns:
    warnings.simplefilter('always')
    test()


if len(wrns):
    print('*' * 79)
    print('warnings: {}'.format(len(wrns)))
    print('first warning:')
    print('{}:{}:{}'.format(wrns[0].filename, wrns[0].lineno, wrns[0].message))
    print('*' * 79)
