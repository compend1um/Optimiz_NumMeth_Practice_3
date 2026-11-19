import numpy as np
import numdifftools as nd
import numpy as np
from math import sqrt, sin, cos, exp

from source.common.gradient_descent import gradient_descent
from source.common.projection import projection_circle


def main_function(point):
    x, y = point
    return sin(1 + x + 2 * exp(y)) * cos(2 * exp(x) - y - 1)


def gradient(point):
    x, y = point

    arg1 = 1 + x + 2 * np.exp(y)
    arg2 = 2 * np.exp(x) - y - 1

    sin1 = np.sin(arg1)
    cos1 = np.cos(arg1)
    sin2 = np.sin(arg2)
    cos2 = np.cos(arg2)

    df_dx = cos1 * cos2 - 2 * np.exp(x) * sin1 * sin2

    df_dy = 2 * np.exp(y) * cos1 * cos2 + sin1 * sin2

    return np.array([df_dx, df_dy])


def remove_duplicates(results, eps=10**(-4)):
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

        if np.linalg.norm(point) < sqrt(7) - 10**(-4):
            results.append((point, value))

    return remove_duplicates(results)
