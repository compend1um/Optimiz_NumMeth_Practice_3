import numpy as np
from math import sqrt, cos, sin, pi

from source.task1.extrema import main_function


def find_boundary_extrema(direction, n = 100000, eps=10**(-3)):
    radius = sqrt(7)

    angles = np.linspace(0, 2 * pi, n, endpoint=False)  # 0 и 2п совпадают

    values = []

    for angle in angles:
        x = radius * cos(angle)
        y = radius * sin(angle)

        point = np.array([x, y])
        value = main_function(point)

        values.append((point, value))

    candidates = []

    for i in range(len(values)):

        previous_value = values[i - 1][1]
        current_value = values[i][1]

        next_index = i + 1
        if next_index == len(values):
            next_index = 0

        next_value = values[next_index][1]

        if direction == 'min':
            if current_value < previous_value and current_value < next_value:
                candidates.append(values[i])

        elif direction == 'max':
            if current_value > previous_value and current_value > next_value:
                candidates.append(values[i])

    results = []

    for point, value in candidates:

        normal = point / radius
        point_in = point - eps * normal

        value_in = main_function(point_in)

        if direction == 'min':
            if value_in > value:
                results.append((point, value))

        elif direction == 'max':
            if value_in < value:
                results.append((point, value))

    unique_results = []

    for point, value in results:
        duplicate = False

        for unique_point, _ in unique_results:
            if np.linalg.norm(point - unique_point) < 10 ** (-4):
                duplicate = True
                break

        if not duplicate:
            unique_results.append((point, value))

    return unique_results