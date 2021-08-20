#!/usr/bin/env python
from collections import Counter
import dis
import sys

import analyse


if __name__ == "__main__":
    if sys.argv[1:] == ["--help"] or len(sys.argv) == 1:
        print(
f"""\
Usage: {sys.argv[0]} [--help] N

Each line from STDIN is a filename to scan for bytecode.

Scan for all bytecode patterns of length N and produce a report on the most
common sequences.\
""")
        exit(0)
    assert len(sys.argv) == 2, "too many arguments"
    N = int(sys.argv[1])
    counter = Counter()
    for bytecode in analyse.find_all():
        for i in range(len(bytecode) - N):
            counter[bytecode[i:i+N]] += 1
    for seq, count in counter.most_common():
        print(count, *(dis.opname[op] for op in seq))
