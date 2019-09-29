curses-key-detector
===================

this script prints out what keys are pressed on the keyboard in curses.  this
is useful for figuring out how to respond to particular key combinations or
escape sequences.

a few things are turned on in this script to make curses give more sequences:
- `os.environ.setdefault('ESCDELAY', '25')` - make the escape key show
  immediately
- `curses.nonl()` the enter key is not transformed to `\n` (such that it can
  be differentiated from `^J`)
- `curses.raw()` `^S` / `^Q` / `^Z` / `^\` are passed through
- `nodelay` loop after escape key detect unknown escape sequences

This can also be useful to see how escape sequences are handled in other
`TERM` situations.

For example, compare `C-Home` / `C-End` on the following terminals:

```console
$ TERM=screen python3 t.py
(sequence) '\x1b[1;5H'
(sequence) '\x1b[1;5F'
```

```console
$ TERM=xterm python3 t.py
535 535 'kHOM5'
530 530 'kEND5'
```
