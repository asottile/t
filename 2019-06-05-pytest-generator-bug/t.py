import pytest


def gen():
    yield 1
    yield 2
    yield 3


m = pytest.mark.parametrize('a', gen())


@m
def test1(a): pass


@m
def test2(a): pass
