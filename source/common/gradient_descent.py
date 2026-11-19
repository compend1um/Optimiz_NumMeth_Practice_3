import numpy as np


def gradient_descent(f, grad, start_point, step=0.01, eps=10 ** (-8), direction='min', projection=None, max_iterations=10000):
    point = np.array(start_point, dtype=float)

    if projection is not None:
        point = projection(point)

    flag = 1 if direction == 'min' else -1

    for iteration in range(max_iterations):
        gradient = np.array(grad(point))

        if np.linalg.norm(gradient) < eps:
            break

        current_value = f(point)
        current_step = step

        while current_step > 10 ** (-12):
            new_point = point - flag * current_step * gradient

            if projection is not None:
                new_point = projection(new_point)

            new_value = f(new_point)

            if flag * (new_value - current_value) < 0:
                break

            current_step /= 2

        if current_step <= 10 ** (-12):
            break

        point = new_point

    return point, f(point)
