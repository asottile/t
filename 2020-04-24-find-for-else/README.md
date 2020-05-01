find-for-else
=============

this is a small ast visitor class which finds `for ...: else:` and
`while ...: else:` statements in python files.  I used this plus [all-repos] to
find some examples for a [youtube video] where I explained the two syntaxes!

here's an example invocation:

```bash
all-repos-find-files --output-paths '\.py$' |
    xargs python t.py 2> /dev/null |
    grep asottile |
    head -5
```

and some output:

```
repos/asottile/add-trailing-comma/add_trailing_comma.py:49
repos/asottile/add-trailing-comma/add_trailing_comma.py:163
repos/asottile/add-trailing-comma/add_trailing_comma.py:226
repos/asottile/add-trailing-comma/add_trailing_comma.py:259
repos/asottile/aspy.refactor_imports/aspy/refactor_imports/classify.py:58
```

[all-repos]: https://github.com/asottile/all-repos
[youtube video]: https://www.youtube.com/watch?v=8P7lXLXR_3c
