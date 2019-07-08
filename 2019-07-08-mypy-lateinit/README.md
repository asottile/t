mypy-lateinit
=============

Demo showing how to convince mypy that lateinit attributes are set to non-None.

with assertion:

```console
$ mypy t.py
$
```

without assertion:

```console
$ mypy t.py
t.py:13: error: Unsupported operand types for + ("None" and "int")
t.py:13: note: Left operand is of type "Optional[int]"
```
