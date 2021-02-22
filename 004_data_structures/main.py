import heapq
from collections import namedtuple
from queue import PriorityQueue
from struct import Struct
from sys import getsizeof
from types import MappingProxyType
from typing import NamedTuple


def test_mapping_proxy_type():
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


def test_struct():
    """https://docs.python.org/3/library/struct.html"""

    MyStruct = Struct('i?f')
    data = MyStruct.pack(123, True, 42.1)
    print(f"Packed data: {data}, unpacked: {MyStruct.unpack(data)}")


def test_heapq():
    q = []
    heapq.heappush(q, (2, 'программировать'))
    heapq.heappush(q, (1, 'есть'))
    heapq.heappush(q, (3, 'спать'))

    print(f"Initial heapq: {q}")

    while q:
        next_item = heapq.heappop(q)
        print(next_item, q)


def test_priorityqueue():
    q = PriorityQueue()
    q.put((2, 'программировать'))
    q.put((1, 'есть'))
    q.put((3, 'спать'))

    print(f"Initial PriorityQueue: {q.queue}")

    while not q.empty():
        next_item = q.get()
        print(next_item, q.queue)


if __name__ == '__main__':
    test_mapping_proxy_type()
    print("--------")

    test_bytes()
    print("--------")

    test_namedtuples()
    print("--------")

    test_struct()
    print("--------")

    test_heapq()
    print("--------")

    test_priorityqueue()
