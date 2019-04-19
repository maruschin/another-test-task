import pytest

from main import Point


A, B = Point(1, 3), Point(3, 1)
C, D = Point(4, 4), Point(-2, 2)


def test_add_function():
    assert A.add(B) == C


def test_sub_function():
    assert A.sub(B) == D


def test_add_operator():
    assert A + B == C


def test_sub_operator():
    assert A - B == D

