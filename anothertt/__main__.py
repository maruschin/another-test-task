import os
import logging

from pathlib import Path
from argparse import ArgumentParser, ArgumentTypeError

from . import Figure


def valid_iterations(string):
    msg = 'The number of iterations must be an integer greater than zero'
    try:
        value = int(string)
    except ValueError:
        raise ArgumentTypeError(msg)
    if value <= 0:
        raise ArgumentTypeError(smg)
    return value


def valid_curvature(string):
    msg = 'The curvature coefficient must be a float between 0 and 1'
    try:
        value = float(string)
    except ValueError:
        raise ArgumentTypeError(msg)
    if not 0 <= value <= 1:
        raise ArgumentTypeError(msg)
    return value


def valid_dimension(string):
    msg = 'Width or height must be an integer greater than zero'
    try:
        value = int(string)
    except ValueError:
        raise ArgumentTypeError(msg)
    if value <= 0:
        raise ArgumentTypeError(msg)
    return value


if __name__ == '__main__':
    FORMAT = '%(asctime)-15s [%(levelname)s] %(message)s'
    FILENAME = "log/example.log"
    log_path = Path('./log')
    try:
        os.makedirs(log_path)
        os.makedirs(log_path/'img')
    except FileExistsError:
        pass
    logging.basicConfig(filename=FILENAME, format=FORMAT, level=logging.DEBUG)
    parser = ArgumentParser(description='Triangular application.')
    parser.add_argument(
        '-W', '--width', default=400,
        type=valid_dimension,
        help='figure width')
    parser.add_argument(
        '-H', '--height', default=600,
        type=valid_dimension,
        help='figure height')
    parser.add_argument(
        '-K', '--curvature', default=0,
        type=valid_curvature,
        help='curvature coefficient')
    parser.add_argument(
        '-N', '--iterations', default=1,
        type=valid_iterations,
        help='number of iterations')
    parser.add_argument(
        '--out', default='fig.png',
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
