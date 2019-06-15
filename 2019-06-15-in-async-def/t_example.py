async def f():
    for x in [3, 4, 5]:
        yield x

    def g():
        for x in [1, 2, 3]:
            yield x

    for x in [3, 4, 5]:
        yield x
    return g
