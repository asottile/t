pytest-generator-bug
====================

demoing a small bug in pytest's `parametrize` when combined with iterator /
generator variable arguments.

discussed on [pytest-dev/pytest#5356]

[pytest-dev/pytest#5356]: https://github.com/pytest-dev/pytest/pull/5356

### demo

```console
$ pytest t.py -v
============================= test session starts ==============================
platform linux -- Python 3.6.7, pytest-4.6.2, py-1.8.0, pluggy-0.12.0 -- /tmp/t/2019-06-05-pytest-generator-bug/venv/bin/python3
cachedir: .pytest_cache
rootdir: /tmp/t/2019-06-05-pytest-generator-bug
collected 4 items

t.py::test1[1] PASSED                                                    [ 25%]
t.py::test1[2] PASSED                                                    [ 50%]
t.py::test1[3] PASSED                                                    [ 75%]
t.py::test2[a0] SKIPPED                                                  [100%]

===================== 3 passed, 1 skipped in 0.01 seconds ======================
```
