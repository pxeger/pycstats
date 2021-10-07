#!/usr/bin/env python
import dis
import marshal
from types import CodeType

def count(results, code):
    results["names"].append(len(code.co_names))
    results["consts"].append(len(code.co_consts))
    for c in code.co_consts:
        if isinstance(c, CodeType):
            count(results, c)


def main():
    print("finding lengths of names and constants")
    results = {
        "names": [],
        "consts": [],
    }
    while True:
        try:
            filename = input()
        except EOFError:
            break
        with open(filename, "rb") as f:
            # skip magic number and metadata
            f.seek(16)
            code = marshal.load(f)
        assert isinstance(code, CodeType)
        count(results, code)

    n = len(results["names"])
    assert n == len(results["consts"])

    for p in range(1, 4):
        p = 256 ** p
        print(f"proportion >={p}:", sum(sum(v) >= p for v in zip(*results.values())) / n)


if __name__ == "__main__":
    main()
