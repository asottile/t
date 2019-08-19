super-wrong-class
=================

This example shows the different invocations of `super(...)` and why the
python 2 form is ~slightly easier to mess up.

This was prompted by reading [pull request] in which it is pointed out that
[pyupgrade] did not rewrite this (pyupgrade is intentionally timid here,
assuming the human knew what they were doing!).

In this toy example, the call to `super(B, self)` from a method in `C` is the
"mistake" in that it isn't looking for the super-call of `C`, but of `B`:

```console
$ python2 t.py
FROM B!
FROM A!
$ python3 t.py
FROM B!
FROM A!
FROM B!
```

[pull request]: https://github.com/marshmallow-code/marshmallow/pull/1276
[pyupgrade]: https://github.com/asottile/pyupgrade
