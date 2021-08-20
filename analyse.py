import dis
import marshal
from types import CodeType


def find_code(code):
    yield code.co_code[::2]
    for c in code.co_consts:
        if isinstance(c, CodeType):
            yield from find_code(c)


def find_all():
    try:
        filename = "true"
        while filename:
            try:
                filename = input()
            except EOFError:
                break
            with open(filename, "rb") as f:
                # skip magic number and metadata
                f.seek(16)
                code = marshal.load(f)
            assert isinstance(code, CodeType)
            for bytecode in find_code(code):
                # print(end=".")
                yield bytecode
            # print()
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt")
        exit(130)
