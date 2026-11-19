import numpy as np
import numdifftools as nd
from math import sqrt, sin, cos, exp

from source.common.gradient_descent import gradient_descent
from source.common.projection import projection_circle


def main_function(point):
    x, y = point
    return sin(1 + x + 2 * exp(y)) * cos(2 * exp(x) - y - 1)


gradient_function = nd.Gradient(main_function)

def gradient(point):
    return gradient_function(point)

def remove_duplicates(results, eps=10**(-2)):
    unique_results = []

    for point, value in results:
        duplicate = False

        for unique_point, unique_value in unique_results:
            if np.linalg.norm(point - unique_point) < eps:
                duplicate = True
                break

        if not duplicate:
            unique_results.append((point, value))

    return unique_results


def find_extrema(direction):
    np.random.seed(42)

    results = []

    angles = np.random.uniform(0, 2 * np.pi, 40)
    radiuses = np.sqrt(np.random.uniform(0, 7, 40))

    start_points = np.column_stack((
        radiuses * np.cos(angles),
        radiuses * np.sin(angles)
    ))

    for start_point in start_points:
        point, value = gradient_descent(
            f=main_function,
            grad=gradient,
            start_point=start_point,
            direction=direction,
            projection=projection_circle,
        )

        if np.linalg.norm(point) < sqrt(7) - 0.01:
            results.append((point, value))

    return remove_duplicates(results)
