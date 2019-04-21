import logging
import functools

from typing import Union, NamedTuple
from random import random
from itertools import combinations
from PIL import Image, ImageDraw
from argparse import ArgumentParser, ArgumentTypeError


class Point(NamedTuple):
    """
    Point class with support for basic arithmetic operations and
    function for middle point.
    """
    x: Union[int, float]
    y: Union[int, float]

    @staticmethod
    def random():
        """Static method returns a random Point in the range from -1 to 1."""
        def rnd():
            return (random()*2 - 1)
        return Point(rnd(), rnd())

    def add(self, other: Union['Point', int]) -> 'Point':
        """Returns the elementwise sum of two points."""
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        else:
            return Point(self.x + other, self.y + other)

    def __add__(self, other: Union['Point', int]) -> 'Point':
        """Add sum operator (+) for elementwise sum of two points."""
        return self.add(other)

    def sub(self, other: Union['Point', int]) -> 'Point':
        """Returns the elementwise difference of two points."""
        if isinstance(other, Point):
            return Point(self.x - other.x, self.y - other.y)
        else:
            return Point(self.x - other, self.y - other)

    def __sub__(self, other: Union['Point', int]) -> 'Point':
        """Add operator (-) for elementwise difference of two points."""
        return self.sub(other)

    def div(self, other: Union['Point', int]) -> 'Point':
        """Returns the elementwise division of two points."""
        if isinstance(other, Point):
            return Point(self.x / other.x, self.y / other.y)
        else:
            return Point(self.x / other, self.y / other)

    def __truediv__(self, other: Union['Point', int]) -> 'Point':
        """Add operator (/) for elementwise division of two points."""
        return self.div(other)

    def mul(self, other: Union['Point', int]) -> 'Point':
        """Returns of elementwise multiplication of two points."""
        if isinstance(other, Point):
            return Point(self.x * other.x, self.y * other.y)
        else:
            return Point(self.x * other, self.y * other)

    def __mul__(self, other: Union['Point', int]) -> 'Point':
        """Add operator (*) for elementwise multiplication of two points."""
        return self.mul(other)

    def __abs__(self) -> 'Point':
        """Return the absolute value of a point."""
        return Point(abs(self.x), abs(self.y))

    def __round__(self) -> 'Point':
        """Returns point with rounded coordinates."""
        return Point(round(self.x), round(self.y))

    def mean_point(self, other: 'Point', k: float) -> 'Point':
        """Returns the midpoint given the randomness coefficient."""
        return round((self + other)/2 + Point.random()*k*abs(self - other))


class Triangle(NamedTuple):
    A: Point
    B: Point
    C: Point

    def get_sides(self):
        points = [self.A, self.B, self.C]
        return combinations(points, 2)

    def __round__(self):
        return Triangle(round(self.A), round(self.B), round(self.C))

    def mutate(self, k: int):
        AB, AC, BC = [A.mean_point(B, k) for A, B in self.get_sides()]
        return [
            Triangle(self.A, AB, AC),
            Triangle(self.B, BC, AB),
            Triangle(self.C, AC, BC),
            ]


class Figure():
    def __init__(self, width: int, height: int, k: float, n: int, out: str):
        self.width = width
        self.height = height
        self.k = k
        self.n = n
        self.out = out

    def init(self) -> 'Triangle':
        A = Point(self.width/2, 0)
        B = Point(0, self.height)
        C = Point(self.width, self.height)
        triangle = round(Triangle(A, B, C))
        self.triangles = [triangle]
        logging.info("First triangle: {}".format(triangle))

    def mutate(self):
        logging.info("Mutate figure:")
        triangles = self.triangles
        for i in range(self.n):
            logging.info("  - Mutation step {}".format(i))
            triangles = [
                tri for triangle in triangles
                    for tri in triangle.mutate(self.k)
                ]
        logging.info("Mutation is complete")
        self.triangles = triangles
    
    def draw(self):
        logging.info("Draw figure:")
        black = (0, 0, 0, 255)
        white = (255, 255, 255, 255)
        canvas = Image.new('RGBA', (self.width, self.height), white)
        draw = ImageDraw.Draw(canvas)
        for i, triangle in enumerate(self.triangles):
            for side in triangle.get_sides():
                draw.line(side, fill=black, width=1)
            if i % 10 == 0:
                logging.info("  - Drawn {} triangles".format(i))
        logging.info("Drawning is complete")
        self.canvas = canvas

    def save(self):
        logging.info("Saving figure to {}".format(self.out))
        self.canvas.save(self.out)
        


def valid_iterations(string):
    msg = 'The number of iterations must be an integer greater than zero'
    try:
        value = int(string)
    except:
        raise ArgumentTypeError(msg)
    if value <= 0:
        raise ArgumentTypeError(msg)
    return value


def valid_curvature(string):
    msg = 'The curvature coefficient must be a float between 0 and 1'
    try:
        value = float(string)
    except:
        raise ArgumentTypeError(msg)
    if not 0 <= value <= 1:
        raise ArgumentTypeError(msg)
    return value


def valid_dimension(string):
    msg = 'Width or height must be an integer greater than zero'
    try:
        value = int(string)
    except:
        raise ArgumentTypeError(msg)
    if value <= 0:
        raise ArgumentTypeError(msg)
    return value


if __name__ == '__main__':
    FORMAT = '%(asctime)-15s [%(levelname)s] %(message)s'
    FILENAME = "example.log"
    logging.basicConfig(filename=FILENAME, format=FORMAT, level=logging.DEBUG)
    parser = ArgumentParser(description='Формирования разбиения фигуры')
    parser.add_argument('-W', '--width', default=400,
        type=valid_dimension,
        help='figure width')
    parser.add_argument('-H', '--height', default=600,
        type=valid_dimension,
        help='figure height')
    parser.add_argument('-K', '--curvature', default=0,
        type=valid_curvature,
        help='curvature coefficient')
    parser.add_argument('-N', '--iterations', default=1,
        type=valid_iterations,
        help='number of iterations')
    parser.add_argument('--out', default='fig.png',
        type=str,
        help='')
    args = parser.parse_args()
    logging.info("Input args: %r", args)
    fig = Figure(
        width=args.width,
        height=args.height,
        k=args.curvature,
        n=args.iterations,
        out=args.out,
    )
    fig.init()
    fig.mutate()
    fig.draw()
    fig.save()

