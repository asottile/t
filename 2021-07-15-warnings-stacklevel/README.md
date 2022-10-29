warnings-stacklevel
===================

a small script I used to check the usage of `warnings.warn` and `stacklevel`
in the standard library to make a case that the default should not be 1 but
instead 2.

```console
$ python3 warnings_warn_stacklevel.py $(git ls-files -- '*.py')
SyntaxError: Lib/lib2to3/tests/data/bom.py
SyntaxError: Lib/lib2to3/tests/data/crlf.py
SyntaxError: Lib/lib2to3/tests/data/different_encoding.py
SyntaxError: Lib/lib2to3/tests/data/false_encoding.py
SyntaxError: Lib/lib2to3/tests/data/py2_test_grammar.py
SyntaxError: Lib/test/bad_coding.py
SyntaxError: Lib/test/bad_coding2.py
SyntaxError: Lib/test/badsyntax_3131.py
SyntaxError: Lib/test/badsyntax_pep3120.py
SyntaxError: Lib/test/test_grammar.py
SyntaxError: Lib/test/test_named_expressions.py
SyntaxError: Lib/test/test_patma.py
SyntaxError: Tools/c-analyzer/c_parser/parser/_delim.py
SyntaxError: Tools/test2to3/maintest.py
SyntaxError: Tools/test2to3/test/test_foo.py
SyntaxError: Tools/test2to3/test2to3/hello.py
{
  "2": 72,
  "4": 1,
  "3": 4,
  "0": 1
}
unparseable: 6
default: 99
```
