simple tokenize-rt code formatter
=================================

my chat wanted me to build a code formatter which performed the following
rewrite:

```python
foo(
    {
        'foo': 'bar',
    }
)
```

to

```python
foo({
    'foo': 'bar',
})
```

and so I built one that kinda works.  there are likely some bugs with
parenthesized things and/or ugly input code, but it should mostly do the job

example:

```console
python3 t.py -
foo(
    {
        'bar': 'baz',
    }
)  # pressed <enter> + ^D here
foo({
    'bar': 'baz',
})
```
