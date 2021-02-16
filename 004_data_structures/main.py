from types import MappingProxyType


def test_MappingProxyType(name):
    read_only = MappingProxyType({"a": 1, "b": 2})
    print(read_only)

    try:
        read_only["a"] = 3
    except TypeError as exc:
        print(exc)


def test_bytes():
    b = bytes((0, 1, 255))
    print(b)
    print(b[1])

    ba = bytearray(b)
    print(ba)
    ba[1] = 25
    print(ba)


if __name__ == '__main__':
    test_MappingProxyType('PyCharm')

    print("--------")

    test_bytes()
