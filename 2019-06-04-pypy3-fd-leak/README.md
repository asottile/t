pypy3-fd-leak
=============

debugging script for pypy3 fd leak in `open`: [pypy/pypy (issue #3021)]

I ended up finding the root cause and fixing this in [pypy/pypy (pr #647)]

[pypy/pypy (issue #3021)]: https://bitbucket.org/pypy/pypy/issues/3021/ioopen-directory-leaks-a-file-descriptor
[pypy/pypy (pr #647)]: https://bitbucket.org/pypy/pypy/pull-requests/647/fix-leak-of-file-descriptor-with-_iofileio/diff

### demo (broken)

```console
$ pypy3  t.py
*******************************************************************************
warnings: 10422
first warning:
t.py:8:unclosed file <_io.FileIO fd=3 mode='rb' closefd=True>
*******************************************************************************
```

### demo (fixed)

```console
$ pypy3 t.py
$
```
