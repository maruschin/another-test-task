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
    Ax, Ay = 1, 3
    Bx, By = 4, 5
    A = Point(Ax, Ay)
    B = Point(Bx, By)
    C1 = Point(Ax + Bx, Ay + By)
    C2 = Point(Ax + 2, Ay + 2)
    assert A.add(B) == C1
    assert A.add(2) == C2


def test_add_operator():
    Ax, Ay = 1, 3
    Bx, By = 4, 5
    A = Point(Ax, Ay)
    B = Point(Bx, By)
    C1 = Point(Ax + Bx, Ay + By)
    C2 = Point(Ax + 2, Ay + 2)
    assert A + B == C1
    assert A + 2 == C2


def test_sub_function():
    Ax, Ay = 1, 3
    Bx, By = 4, 5
    A = Point(Ax, Ay)
    B = Point(Bx, By)
    C1 = Point(Ax - Bx, Ay - By)
    C2 = Point(Ax - 2, Ay - 2)
    assert A.sub(B) == C1
    assert A.sub(2) == C2


def test_sub_operator():
    Ax, Ay = 1, 3
    Bx, By = 4, 5
    A = Point(Ax, Ay)
    B = Point(Bx, By)
    C1 = Point(Ax - Bx, Ay - By)
    C2 = Point(Ax - 2, Ay - 2)
    assert A - B == C1
    assert A - 2 == C2


def test_div_function():
    Ax, Ay = 1, 3
    Bx, By = 4, 5
    A = Point(Ax, Ay)
    B = Point(Bx, By)
    C1 = Point(Ax / Bx, Ay / By)
    C2 = Point(Ax / 2, Ay / 2)
    assert A.div(B) == C1
    assert A.div(2) == C2


def test_div_operator():
    Ax, Ay = 1, 3
    Bx, By = 4, 5
    A = Point(Ax, Ay)
    B = Point(Bx, By)
    C1 = Point(Ax / Bx, Ay / By)
    C2 = Point(Ax / 2, Ay / 2)
    assert A / B == C1
    assert A / 2 == C2


def test_mul_function():
    Ax, Ay = 1, 3
    Bx, By = 4, 5
    A = Point(Ax, Ay)
    B = Point(Bx, By)
    C1 = Point(Ax * Bx, Ay * By)
    C2 = Point(Ax * 2, Ay * 2)
    assert A.mul(B) == C1
    assert A.mul(2) == C2


def test_mul_operator():
    Ax, Ay = 1, 3
    Bx, By = 4, 5
    A = Point(Ax, Ay)
    B = Point(Bx, By)
    C1 = Point(Ax * Bx, Ay * By)
    C2 = Point(Ax * 2, Ay * 2)
    assert A * B == C1
    assert A * 2 == C2


def test_abs_function():
    A = Point(1, 2)
    B = A * -1
    assert A == abs(B)


def test_random_point():
    seed(1337)
    A = Point.random(0.5)
    B = Point(0.11775285695147064, 0.03326557360500082)
    assert A == B


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

