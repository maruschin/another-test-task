from collections import namedtuple
from typing import Union
from random import random


w, h = 400, 600
k = 0.5


BasePoint = namedtuple('Point', ('x', 'y'))


class Point(BasePoint):
    @staticmethod
    def random(k: float):
        rnd = lambda k: (random()*2 - 1)*k
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

