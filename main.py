from typing import Union, NamedTuple
from random import random
from itertools import combinations
from PIL import Image, Image


class Point(NamedTuple):
    x: Union[int, float]
    y: Union[int, float]

    @staticmethod
    def random():
        def rnd():
            return (random()*2 - 1)
        return Point(rnd(), rnd())

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

    def __round__(self) -> 'Point':
        return Point(round(self.x), round(self.y))


class Triangle(NamedTuple):
    A: Point
    B: Point
    C: Point

    def _get_points(self):
        return [self.A, self.B, self.C]

    def get_sides(self):
        return combinations(self._get_points(), 2)

    def __round__(self):
        return Triangle(round(self.A), round(self.B), round(self.C))

    @staticmethod
    def mean_point(A: Point, B: Point, k: int) -> Point:
        return round((A + B)/2 + Point.random()*k*abs(A - B))

    def mutate(self, k: int):
        AB, AC, BC = [
            self.mean_point(A, B, k) for A, B
            in self.get_sides()
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
    return round(Triangle(A, B, C))


def draw(tri: Triangle):
    black = (0, 0, 0, 255)
    white = (255, 255, 255, 255)
    canvas = Image.new('RGBA', (1000, 1000), white)
    draw = ImageDraw.Draw(canvas)


if __name__ == '__main__':
    w, h = 400, 600
    k = 0.5
    tri = get_init_triangle(400, 600)
    print(tri)
    print([round(fig) for fig in tri.mutate(0.2)])

