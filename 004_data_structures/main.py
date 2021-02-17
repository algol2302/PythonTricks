from types import MappingProxyType
from collections import namedtuple
from typing import NamedTuple
from sys import getsizeof
from struct import Struct


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


def test_namedtuples():
    simple_car = ('red', 123)
    print(f"Repr: {simple_car}, size: {getsizeof(simple_car)}")

    Car1 = namedtuple('Auto', 'color mileage')
    car1 = Car1('red', 123)
    print(
        f"Repr: {car1}, "
        f"properties: {car1.color, car1.mileage}, "
        f"size: {getsizeof(car1)}"
    )

    class Car(NamedTuple):
        color: str
        mileage: int

    car2 = Car(color='red', mileage=123)
    print(
        f"Repr: {car2}, "
        f"properties: {car2.color, car2.mileage}, "
        f"size: {getsizeof(car2)}"
    )


def test_Struct():
    """https://docs.python.org/3/library/struct.html"""

    MyStruct = Struct('i?f')
    data = MyStruct.pack(123, True, 42.1)
    print(f"Packed data: {data}, unpacked: {MyStruct.unpack(data)}")


if __name__ == '__main__':
    test_MappingProxyType('PyCharm')
    print("--------")

    test_bytes()
    print("--------")

    test_namedtuples()
    print("--------")

    test_Struct()
