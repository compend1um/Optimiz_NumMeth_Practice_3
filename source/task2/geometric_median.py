from data_generation import generate_points
from source.common.gradient_descent import gradient_descent
import numpy as np

__all__ = ['main_func']


def _make_f(points):
    def f(a):
        return np.sum(np.linalg.norm(points - a, axis=1))
    return f


# 2. Градиент grad(a) = сумма (a - x_i) / ||a - x_i||
def _make_grad(points):
    def grad(a):
        diff = a - points                           # Векторы от точек к a
        dist = np.linalg.norm(diff, axis=1)    # Расстояния
        dist = np.maximum(dist, 1e-12)         # Защита от деления на 0
        return np.sum(diff / dist[:, None], axis=0) # Сумма единичных векторов
    return grad


def _sum_from_a_to_points(points, a):
    return np.sum(np.linalg.norm(points - a, axis=1))


def main_func():

    points = generate_points(50)

    arithmetic_mean_point = points.mean(axis=0)
    arithmetic_mean_value = _sum_from_a_to_points(points, arithmetic_mean_point)

    # print(arithmetic_mean_point)

    geometric_median_point, geometric_median_value = gradient_descent(
        _make_f(points), _make_grad(points), arithmetic_mean_point
    )

    print(
        "арифметическое среднее\n",
        f"точка: {arithmetic_mean_point}\t значение: {arithmetic_mean_value}\n\n",

        "геометрическая медиана\n",
        f"точка {geometric_median_point}\t значение: {geometric_median_value}",
        sep=""
    )

    return None


main_func()


