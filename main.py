from collections import namedtuple



w, h = 400, 600
k = 0.5



BasePoint = namedtuple('Point', ('x', 'y'))
class Point(BasePoint):
    def add(self, other: 'Point') -> 'Point':
        return Point(self.x + other.x, self.y + other.y)


    def sub(self, other: 'Point') -> 'Point':
        return Point(self.x - other.x, self.y - other.y)



A, B = Point(2,3), Point(1,2)
print('A = {}, B = {}'.format(A, B))
print('test A.add(B):', A.add(B))
print('test A.sub(B):', A.sub(B))

