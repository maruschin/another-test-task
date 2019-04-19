from collections import namedtuple



w, h = 400, 600
k = 0.5



BasePoint = namedtuple('Point', ('x', 'y'))
class Point(BasePoint):
    def add(self, other: 'Point') -> 'Point':
        return Point(self.x + other.x, self.y + other.y)


    def __add__(self, other: 'Point') -> 'Point':
        return self.add(other)


    def sub(self, other: 'Point') -> 'Point':
        return Point(self.x - other.x, self.y - other.y)


    def __sub__(self, other: 'Point') -> 'Point':
        return self.sub(other)


    def __eq__(self, other: 'Point') -> bool:
        return (self.x == other.x) and (self.y == other.y)

