module-metaclass
================

The `__module__` attribute is not inherited (intentionally, it usually points
to where the class was defined).  In [pytest-dev/pytest#5452] it was pointed
out that it was desirable to have all pytest exceptions / warnings produce
their `__module__` using the public module path.

```pycon
>>> class C:
...     __module__ = 'hi'
...
>>> class D(C): pass
...
>>> D.__module__
'__main__'
>>> C.__module__
'hi'
```

This demo shows how you could use a metaclass to ensure `__module__` gets set
in a specific way.  I wanted to make this syntax work, but I couldn't get
subclasses to initialize properly:

```python
class C(metaclass=mcs, module='pytest'): pass
```

I think I'll have to read more into [PEP 487]...

[pytest-dev/pytest#5452]: https://github.com/pytest-dev/pytest/pull/5452
[PEP 487]: https://www.python.org/dev/peps/pep-0487/
