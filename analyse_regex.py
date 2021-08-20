#!/usr/bin/env python
import dis
import regex
import sys

import analyse


def esc(n):
    return f"\\x{n:02x}"


if __name__ == "__main__":
    if sys.argv[1:] == ["--help"] or len(sys.argv) == 1:
        print(
f"""\
Usage:
{sys.argv[0]} [--help]
{sys.argv[0]} pattern [pattern ...]

Each line from STDIN is a filename to scan for bytecode.

Each pattern is concatenated to form a regular expression. The pattern may
contain the names of opcodes, which will match operations in the bytecode.\
""")
        exit(0)
    pattern = regex.compile("".join(
        esc(dis.opmap[op]) if op in dis.opmap else op
        for op in sys.argv[1:]
    ).encode("ascii"))
    count = 0
    for bytecode in analyse.find_all():
        for _ in pattern.finditer(bytecode, overlapped=True):
            # print(end="+")
            count += 1
    print()
    print(count)
