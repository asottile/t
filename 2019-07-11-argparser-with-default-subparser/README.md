argparser-with-default-subparser
================================

this is a hacky attempt to implement passthrough but also adding custom
commands.  the idea being you could extend an existing executable with
new subparsers but without needing to enumerate their existing parsers.

example usage:

```console
$ python3 t.py foo wat
do foo wat
$ python3 t.py pass through
passthrough: pass ['through']
```
