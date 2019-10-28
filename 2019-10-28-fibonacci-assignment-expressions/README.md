fibonnacci-assignemnt-expressions
=================================

```python
# fits in 80 characters, wow!
fib = lambda n:[(a:=0),(b:=1)]+[(c:=a)+(a:=b)+(b:=a+c)-a-c for _ in range(n-2)]
```

```pycon
>>> fib(10)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
>>> fib(15)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
```

A haxy code-golfed lambda implementing the fibbonnacci sequence using python3.8
assignment expressions.

The interesting bits of this are:
- add-swap implemented with a third helper variable
- linear and non-recursive

Originally posted as a [tweet] as a response to the change in execution order
for keys / values in [dictionary comprehensions][python/cpython#14139].

[tweet]: https://twitter.com/codewithanthony/status/1140847842145161216
[python/cpython#14139]: https://github.com/python/cpython/pull/14139
