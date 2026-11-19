
import numpy as np
from math import sqrt, cos, sin, pi

from source.task1.extrema import main_function


def find_boundary_extrema(direction, n=100000, eps=10**(-3)):

    radius = sqrt(7)
    angles = np.linspace(0, 2 * pi, n, endpoint=False)

    values = []

    for angle in angles:
        point = np.array([
            radius * cos(angle),
            radius * sin(angle)
        ])

        values.append((point, main_function(point)))

    results = []

    for i in range(n):
        previous_value = values[i - 1][1]
        current_value = values[i][1]
        next_value = values[(i + 1) % n][1]

        if direction == 'min':
            is_extreme = current_value < previous_value and current_value < next_value
        else:
            is_extreme = current_value > previous_value and current_value > next_value

        if not is_extreme:
            continue

        point, value = values[i]

        normal = point / radius
        point_in = point - eps * normal
        value_in = main_function(point_in)

        if direction == 'min' and value_in > value:
            results.append((point, value))

        elif direction == 'max' and value_in < value:
            results.append((point, value))

    unique_results = []

    for point, value in results:
        duplicate = False

        for unique_point, _ in unique_results:
            if np.linalg.norm(point - unique_point) < 10**(-4):
                duplicate = True
                break

        if not duplicate:
            unique_results.append((point, value))

    return unique_results
