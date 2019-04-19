from collections import namedtuple
from typing import Union



w, h = 400, 600
k = 0.5



BasePoint = namedtuple('Point', ('x', 'y'))
class Point(BasePoint):
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


    def __eq__(self, other: Union['Point', int]) -> bool:
        return (self.x == other.x) and (self.y == other.y)

