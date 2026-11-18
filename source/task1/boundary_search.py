import numpy as np
from math import sqrt, sin, cos, pi

from source.task1.extrema import main_function


def find_boundary_extrema(direction):

    radius = sqrt(7)

    angles = np.linspace(0, 2 * pi, 20000, endpoint=False) #т.к 0 и 2п совпадают

    values = []

    for angle in angles:
        x = radius * cos(angle)
        y = radius * sin(angle)

        point = np.array([x, y])
        value = main_function(point)

        values.append((point, value))

    results = []

    for i in range(len(values)):

        previous_value = values[i - 1][1]
        current_value = values[i][1]

        next_index = i + 1

        if next_index == len(values):
            next_index = 0

        next_value = values[next_index][1]

        if direction == 'min':
            if current_value < previous_value and current_value < next_value:
                results.append(values[i])

        elif direction == 'max':
            if current_value > previous_value and current_value > next_value:
                results.append(values[i])


    unique_results = []

    for point, value in results:
        duplicate = False

        for unique_point, _ in unique_results:
            if np.linalg.norm(point - unique_point) < 10**(-2):
                duplicate = True
                break

        if not duplicate:
            unique_results.append((point, value))

    return unique_results


