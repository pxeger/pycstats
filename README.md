# pycstats
Statistics on Python bytecode

Requirements:
- CPython 3.9+
- pip
- bash
- curl
- jq

Tested on GNU/Linux and probably won't work anywhere else.

```bash
$ # download all packages and compile bytecode
$ ./download.sh
$ # analyse pyc files with regex-ish
$ # (e.g. look for LOAD_CONST followed by anything other than RETURN_VALUE)
$ find . -name '*.pyc' | ./analyse.py LOAD_CONST '(?!' RETURN_VALUE ')'
...............
245
```
