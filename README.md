# pycstats
Statistics on Python bytecode

Requirements:
- CPython 3.9+
- pip
- [regex](https://pypi.org/project/regex/)
- bash
- curl
- jq
- unzip
- find

Tested on GNU/Linux and probably won't work anywhere else.

```bash
$ # download all packages and compile bytecode
$ ./download.sh
$ # analyse pyc files with regex-ish
$ # (e.g. look for LOAD_CONST followed by anything other than RETURN_VALUE)
$ find . -name '*.pyc' | ./analyse_regex.py LOAD_CONST '(?!' RETURN_VALUE ')'
...............
245
$ # scan all length-3 opcode sequences
$ find . -name '*.pyc' | ./analyse_sequences.py 3
208838 LOAD_CONST LOAD_CONST LOAD_CONST
165043 LOAD_CONST LOAD_CONST MAKE_FUNCTION
107435 STORE_NAME LOAD_CONST LOAD_CONST
103254 LOAD_CONST MAKE_FUNCTION STORE_NAME
81826 MAKE_FUNCTION STORE_NAME LOAD_CONST
[...]
```

To use with the Python standard library:

```bash
$ sudo python -m compileall
$ find . /usr/lib/python3.9/ -name '*.pyc' | ./analyse_[...]
```
