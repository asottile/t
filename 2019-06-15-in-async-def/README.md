in-async-def
============

A short demo `ast` visitor for properly handling the context of being inside
of an `async def`.

This was done because of a bug found in `pyupgrade` which was accidentally
rewriting to `yield from` inside an `async def` where that's not allowed!

See [pyupgrade#167] for more details.

[pyupgrade#167]: https://github.com/asottile/pyupgrade/issues/167

Example output:

```console
$ python3 t.py t_example.py
got `for` on line 2 | True
got `for` on line 6 | False
got `for` on line 9 | True
```
