unicode-exceptions-py2
======================

A small demo of exceptions requiring native strings (and the associated
crash in python2).

```console
$ python2 t.py
E
======================================================================
ERROR: test_thing (__main__.MyTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "t.py", line 11, in test_thing
    assert_raises_regex(Exception, u'\u2603', f)
  File "/usr/lib/python2.7/unittest/case.py", line 993, in assertRaisesRegexp
    callable_obj(*args, **kwargs)
  File "/usr/lib/python2.7/unittest/case.py", line 127, in __exit__
    if not expected_regexp.search(str(exc_value)):
UnicodeEncodeError: 'ascii' codec can't encode character u'\u2603' in position 0: ordinal not in range(128)

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (errors=1)
```

A python2+python3 compatible way is to convert the values to native strings:

```python
raise Exception(u'\u2603'.encode('UTF-8') if PY2 else u'\u2603')
```

From a discussion on [pytest-dev/pytest#5478]


[pytest-dev/pytest#5478]: https://github.com/pytest-dev/pytest/issues/5478
