import os
import sys
import logging
import functools
import datetime
import uuid

from pathlib import Path
from typing import Union, NamedTuple
from random import random
from itertools import combinations
from PIL import Image, ImageDraw


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
    """
    Triangle class that implements the necessary functions
    for splitting and drawing.
    """
    A: Point
    B: Point
    C: Point

    def get_sides(self):
        """Returns the points of the sides of a triangle"""
        points = [self.A, self.B, self.C]
        return combinations(points, 2)

    def __round__(self):
        """Returns Triangle with rounded points."""
        return Triangle(round(self.A), round(self.B), round(self.C))

    def mutate(self, k: int):
        """Returns splitting a triangle into new three triangles."""
        AB, AC, BC = [A.mean_point(B, k) for A, B in self.get_sides()]
        return [
            Triangle(self.A, AB, AC),
            Triangle(self.B, BC, AB),
            Triangle(self.C, AC, BC),
            ]


class MutateFigureError(AttributeError):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


class Figure():
    def __init__(self, width: int, height: int, k: float, n: int, out: str):
        self.width = width
        self.height = height
        self.k = k
        self.n = n
        self.out = out

    def init(self):
        """Method to create the first shape."""
        A = Point(self.width/2, 0)
        B = Point(0, self.height)
        C = Point(self.width, self.height)
        triangle = round(Triangle(A, B, C))
        self.triangles = [triangle]
        logging.info("First triangle: {}".format(triangle))

    def mutate(self):
        """The method of transforming the shape of a given algorithm."""
        logging.info("Mutate figure:")
        try:
            triangles = self.triangles
        except AttributeError as e:
            logging.fatal(
                "You must initialize the object before mutation",
                exc_info=True)
            sys.exit(1)
        for i in range(self.n):
            logging.info("  - Mutation step {}".format(i+1))
            triangles = [tri
                         for triangle in triangles
                         for tri in triangle.mutate(self.k)]
        logging.info("Mutation is complete")
        self.triangles = triangles

    def draw(self):
        """Method fo drawing shapes on canvas."""
        logging.info("Draw figure:")
        black = (0, 0, 0, 255)
        white = (255, 255, 255, 255)
        canvas = Image.new('RGBA', (self.width, self.height), white)
        draw = ImageDraw.Draw(canvas)
        try:
            triangles = self.triangles
        except AttributeError as e:
            logging.fatal(
                "You must initialize the object before mutation and draw",
                exc_info=True)
            sys.exit(1)
        if len(triangles) == 1:
            raise MutateFigureError('You must mutate figure before drawing.')
        for i, triangle in enumerate(self.triangles):
            for side in triangle.get_sides():
                draw.line(side, fill=black, width=1)
            if i % 10 == 0:
                logging.info("  - Drawn {} triangles".format(i))
        logging.info("Drawning is complete")
        self.canvas = canvas

    def save(self):
        log_img_name = Path('.')/"log"/"img"/"fig{}.png".format(
            #datetime.datetime.now(),
            uuid.uuid4())
        try:
            canvas = self.canvas
        except AttributeError as e:
            logging.fatal(
                "You must draw figure before save",
                exc_info=True)
            sys.exit(1)
        logging.info("Saving figure to {}".format(self.out))
        self.canvas.save(self.out)
        logging.info("Saving log to {}".format(log_img_name))
        self.canvas.save(log_img_name)


if __name__ == '__main__':
    pass
