import pytest

from main import Point


A, B = Point(1, 3), Point(3, 1)
# For equation:
#   A + B = C
#   A - B = D
C, D = Point(4, 4), Point(-2, 2)
# For equation:
#   A + 2 = E
#   A - 2 = F
E, F = Point(3, 5), Point(-1, 1)


def test_add_function():
    assert A.add(B) == C
    assert A.add(2) == E


def test_sub_function():
    assert A.sub(B) == D
    assert A.sub(2) == F


def test_add_operator():
    assert A + B == C
    assert A + 2 == E


def test_sub_operator():
    assert A - B == D
    assert A - 2 == F

