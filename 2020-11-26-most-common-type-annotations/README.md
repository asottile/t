most-common-type-annotations
============================

an ast visitor which prints the most common type annotations

for example:

```console
$ git ls-files -- '*.py' | xargs python3.10 t.py
[(('prefix', 'Prefix'), 47),
 (('version', 'str'), 27),
 (('hook', 'Hook'), 26),
 (('color', 'bool'), 24),
 (('file_args', 'Sequence[str]'), 20),
 (('store', 'Store'), 16),
 (('additional_dependencies', 'Sequence[str]'), 16),
 (('language_version', 'str'), 16),
 (('venv', 'str'), 13),
 (('filename', 'str'), 12),
 (('path', 'str'), 11),
 (('config_file', 'str'), 11),
 (('repo', 'str'), 8),
 (('hook_type', 'str'), 8),
 (('**kwargs', 'Any'), 8),
 (('argv', 'Sequence[str] | None'), 7),
 (('dct', 'dict[str, Any]'), 7),
 (('cmd', 'tuple[str, ...]'), 7),
 (('args', 'Sequence[str]'), 6),
 (('environ', 'MutableMapping[str, str]'), 6)]
```
