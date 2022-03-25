from __future__ import annotations


async def f():
    for x in [3, 4, 5]:
        yield x

    def g():
        yield from [1, 2, 3]

    for x in [3, 4, 5]:
        yield x
    return g
