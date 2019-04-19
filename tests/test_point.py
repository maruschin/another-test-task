import pytest

from main import Point
from random import seed


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


def test_div_function():
    assert Point(1, 3).div(Point(3, 1)) == Point(1/3, 3/1)
    assert Point(2, 1).div(2) == Point(2/2, 1/2)


def test_div_operator():
    assert Point(1, 3) / Point(3, 1) == Point(1/3, 3/1)
    assert Point(1, 2) / 2 == Point(1/2, 2/2)


def test_mul_function():
    assert Point(1, 3).mul(Point(3, 1)) == Point(1*3, 3*1)
    assert Point(2, 1).mul(2) == Point(2*2, 1*2)


def test_mul_operator():
    assert Point(1, 3) * Point(3, 1) == Point(1*3, 3*1)
    assert Point(1, 2) * 2 == Point(1*2, 2*2)


def test_abs_function():
    assert Point(1, 1) == abs(Point(-1, -1))


def test_random_point():
    seed(1337)
    assert Point.random(0.5) == Point(0.11775285695147064, 0.03326557360500082)


def test_mean_point():
    Rnd = Point.random(0.5)
    Rndx, Rndy = Rnd.x, Rnd.y
    Ax, Ay = 1, 1
    Bx, By = 7, 7
    Cx = (Ax + Bx)/2 + abs(Ax - Bx)*Rndx
    Cy = (Ay + By)/2 + abs(Ay - By)*Rndy
    A = Point(Ax, Ay)
    B = Point(Bx, By)
    C = Point(Cx, Cy)
    assert (A + B)/2 + Rnd*abs(A - B) == C

