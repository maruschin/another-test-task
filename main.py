from collections import namedtuple



w, h = 400, 600
k = 0.5



BasePoint = namedtuple('Point', ('x', 'y'))
class Point(BasePoint):
    def add(self, other: 'Point'):
        return Point(self.x + other.x, self.y + other.y)


    def sub(self, other: 'Point'):
        return Point(self.x - other.x, self.y - other.y)


print(Point(2,3).add(Point(2,3)).sub(Point(1.2, 3.4)))
