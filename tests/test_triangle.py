import pytest

from anothertt import Point, Triangle


def test_round_method():
    A = Point(1.2, 2.3)
    B = Point(4.2, 5.2)
    C = Point(5.3, 5.2)
    ABC1 = Triangle(A, B, C)
    ABC2 = Triangle(round(A), round(B), round(C))
    assert round(ABC1) == ABC2
