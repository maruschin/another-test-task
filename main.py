from typing import Union, NamedTuple
from random import random
from itertools import combinations


w, h = 400, 600
k = 0.5


class Point(NamedTuple):
    x: Union[int, float]
    y: Union[int, float]

    @staticmethod
    def random(k: float):
        def rnd(k): (random()*2 - 1)*k
        return Point(rnd(k), rnd(k))

    def add(self, other: Union['Point', int]) -> 'Point':
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        else:
            return Point(self.x + other, self.y + other)

    def __add__(self, other: Union['Point', int]) -> 'Point':
        return self.add(other)

    def sub(self, other: Union['Point', int]) -> 'Point':
        if isinstance(other, Point):
            return Point(self.x - other.x, self.y - other.y)
        else:
            return Point(self.x - other, self.y - other)

    def __sub__(self, other: Union['Point', int]) -> 'Point':
        return self.sub(other)

    def div(self, other: Union['Point', int]) -> 'Point':
        if isinstance(other, Point):
            return Point(self.x / other.x, self.y / other.y)
        else:
            return Point(self.x / other, self.y / other)

    def __truediv__(self, other: Union['Point', int]) -> 'Point':
        return self.div(other)

    def mul(self, other: Union['Point', int]) -> 'Point':
        if isinstance(other, Point):
            return Point(self.x * other.x, self.y * other.y)
        else:
            return Point(self.x * other, self.y * other)

    def __mul__(self, other: Union['Point', int]) -> 'Point':
        return self.mul(other)

    def abs(self) -> 'Point':
        return Point(abs(self.x), abs(self.y))

    def __abs__(self) -> 'Point':
        return self.abs()

    def __eq__(self, other: Union['Point', int]) -> bool:
        return (self.x == other.x) and (self.y == other.y)


class Triangle(NamedTuple):
    A: Point
    B: Point
    C: Point

    def _get_points(self):
        return [self.A, self.B, self.C]

    @staticmethod
    def _get_random_mean_point(A: Point, B: Point, k: int) -> Point:
        return (A + B)/2 + Point.random(k)*abs(A - B)

    def mutate(self, k: int):
        AB, AC, BC = [
            self._get_random_mean_point(A, B, k) for A, B
            in combinations(self._get_points(), 2)
            ]
        return [
            Triangle(self.A, AB, AC),
            Triangle(self.B, BC, AB),
            Triangle(self.C, AC, BC),
            ]


def get_init_triangle(w: int, h: int) -> Triangle:
    A = Point(w/2, 0)
    B = Point(0, h)
    C = Point(w, h)
    return Triangle(A, B, C)


if __name__ == '__main__':
    tri = get_init_triangle(400, 600)
    print(tri)
    print(tri.mutate(0.2))

