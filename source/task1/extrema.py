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

    df_dx = np.cos(arg1) * np.cos(arg2) - 2 * np.exp(x) * np.sin(arg1) * np.sin(arg2)
    df_dy = 2 * np.exp(y) * np.cos(arg1) * np.cos(arg2) + np.sin(arg1) * np.sin(arg2)

    return np.array([df_dx, df_dy])


def is_critical_point(point):
    return np.linalg.norm(gradient(point)) < 10**(-4)


def is_local_extremum(point, direction):
    value = main_function(point)
    eps = 10**(-4)

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    for dx, dy in directions:
        new_point = point + eps * np.array([dx, dy])
        new_value = main_function(new_point)

        if direction == 'min' and new_value < value:
            return False

        if direction == 'max' and new_value > value:
            return False

    return True


def remove_duplicates(results, eps=10**(-4)):
    unique_results = []

    for point, value in results:
        duplicate = False

        for unique_point, _ in unique_results:
            if np.linalg.norm(point - unique_point) < eps:
                duplicate = True
                break

        if not duplicate:
            unique_results.append((point, value))

    return unique_results


def find_extrema(direction):
    np.random.seed(42)

    results = []

    angles = np.random.uniform(0, 2 * np.pi, 1000)
    radiuses = np.sqrt(np.random.uniform(0, 7, 1000))

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
            projection=projection_circle
        )

        if np.linalg.norm(point) >= sqrt(7) - 10**(-4):
            continue

        if not is_critical_point(point):
            continue

        if not is_local_extremum(point, direction):
            continue

        results.append((point, value))

    return remove_duplicates(results)