import numpy as np


def gradient_descent(f, grad, start_point, step=0.01, eps= 10**(-8), direction='min', projection=None, max_iterations=4000):

    point = np.array(start_point)

    if projection is not None:
        point = projection(point)

    flag = 1 if direction == 'min' else -1

    for iteration in range(max_iterations):
        gradient = np.array(grad(point))
        new_point = point - flag * step * gradient

        if projection is not None:
            new_point = projection(new_point)

        if np.linalg.norm(new_point - point) < eps: #вычисление длины вектора между двумя точками sqrt(x**2+y**2)
            point = new_point
            break

        point = new_point

    return point, f(point)

