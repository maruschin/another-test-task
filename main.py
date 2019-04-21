import logging
import functools

from typing import Union, NamedTuple
from random import random
from itertools import combinations
from PIL import Image, ImageDraw
from argparse import ArgumentParser, ArgumentTypeError


def func_logging(func):
    @functools.wraps(func)
    def func_log(*args, **kwargs):
        logging.info("Run function: {0}{1})".format(func.__name__))
        return func(*args, **kwargs)
    return func_log


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
        AB, AC, BC = [self.mean_point(A, B, k) for A, B in self.get_sides()]
        return [
            Triangle(self.A, AB, AC),
            Triangle(self.B, BC, AB),
            Triangle(self.C, AC, BC),
            ]


class Figure():
    def __init__(self, width: int, height: int, k: float):
        self.width = width
        self.height = height
        self.k = k

    def init(self) -> 'Triangle':
        A = Point(self.width/2, 0)
        B = Point(0, self.height)
        C = Point(self.width, self.height)
        self.triangles = [round(Triangle(A, B, C))]

    def mutate(self, n: int):
        triangles = self.triangles
        for i in range(n):
            triangles = [
                tri for triangle in triangles
                    for tri in triangle.mutate(self.k)
                ]
        self.triangles = triangles

    def draw(self):
        black = (0, 0, 0, 255)
        white = (255, 255, 255, 255)
        canvas = Image.new('RGBA', (self.width, self.height), white)
        draw = ImageDraw.Draw(canvas)
        for triangle in self.triangles:
            for side in triangle.get_sides():
                draw.line(side, fill=black, width=1)
        return canvas


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
    FORMAT = '%(asctime-15s [%(levelname)s] %(message)s'
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
    args = parser.parse_args()
    print(args)
    fig = Figure(
        width=args.width,
        height=args.height,
        k=args.curvature,
    )
    fig.init()
    fig.mutate(args.iterations)
    canvas = fig.draw()
    canvas.save('fig.png')

