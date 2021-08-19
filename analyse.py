#!/usr/bin/env python
import dis
import marshal
import re
import sys
from types import CodeType
from collections.abc import Iterable


def get_code_objects_from_pyc_file(path: str) -> Iterable[CodeType]:
    with open(path, "rb") as f:
        f.seek(16)
        code = marshal.load(f)
    return find_code_objects_recursively(code)


def find_code_objects_recursively(code: CodeType) -> Iterable[CodeType]:
    yield code
    for c in code.co_consts:
        if isinstance(c, CodeType):
            yield from find_code_objects_recursively(c)


def get_code_instructions(path: str) -> bytearray:
    b = bytearray()
    for c in get_code_objects_from_pyc_file(path):
        b.extend(c.co_code[::2])
    return b


def esc(n):
    return "\\x" + hex(n)[2:].zfill(2)


if __name__ == "__main__":
    if sys.argv[1:] == ["--help"]:
        print(
f"""\
Usage: {sys.argv[0]} [-h | --help] [opcode ...]

Each line from STDIN is a filename to scan for bytecode.\
""")
        exit(0)
    count = 0
    try:
        assert len(sys.argv) >= 1
        pattern = re.compile("".join(esc(dis.opmap[op]) if op in dis.opmap else op for op in sys.argv[1:]).encode("ascii"))
        filename = "true"
        while filename:
            try:
                filename = input()
            except EOFError:
                break
            bytecode = get_code_instructions(filename)
            print(end=".")
            for _ in pattern.finditer(bytecode):
                print(end="+")
                count += 1
        print()
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt")
        exit(130)
    finally:
        print(count)
