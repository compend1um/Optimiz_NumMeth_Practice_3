from source.common.gradient_descent import gradient_descent
import numpy as np

# __all__ = ['main_func']


def make_f(points):
    def f(a):
        return np.sum(np.linalg.norm(points - a, axis=1))
    return f


# 2. Градиент grad(a) = сумма (a - x_i) / ||a - x_i||
def make_grad(points):
    def grad(a):
        diff = a - points                           # Векторы от точек к a
        dist = np.linalg.norm(diff, axis=1)    # Расстояния
        dist = np.maximum(dist, 1e-12)         # Защита от деления на 0
        return np.sum(diff / dist[:, None], axis=0) # Сумма единичных векторов
    return grad


def _sum_from_a_to_points(points, a):
    return np.sum(np.linalg.norm(points - a, axis=1))


def calculate_arithmetic_mean(points):

    point = points.mean(axis=0)
    value = _sum_from_a_to_points(points, point)

    return point, value


def calculate_geometric_median(points, arithmetic_mean_point):

    point, value = gradient_descent(make_f(points), make_grad(points), arithmetic_mean_point)

    return point, value


def print_result_without_outlier(
        arithmetic_mean_point, arithmetic_mean_value,
        geometric_median_point, geometric_median_value
):
    """
    Найти геометрическую медиану и сравнить её со средним арифметическим
    :param points: точки, для которых осуществлияются вычисления и сравнение
    :return: -
    """


    print(
        "арифметическое среднее\n",
        f"точка: {arithmetic_mean_point}\t значение: {arithmetic_mean_value}\n\n",

        "геометрическая медиана\n",
        f"точка {geometric_median_point}\t значение: {geometric_median_value}\n\n",

        f"Расстояние между ними: {np.linalg.norm(arithmetic_mean_point - geometric_median_point)}\n\n",
        sep=""
    )

    return None



def print_result_with_outlier(
        arithmetic_mean_point_out, arithmetic_mean_value_out,
        geometric_median_point_out, geometric_median_value_out
):

    print(
        "=== С ВЫБРОСОМ ===\n\n",
        "арифметическое среднее\n",
        f"точка: {arithmetic_mean_point_out}, значение = {arithmetic_mean_value_out}\n\n",

        "геометрическая медиана\n"
        f"точка: {geometric_median_point_out}, значение = {geometric_median_value_out}\n",
          )


def compare(arithmetic_mean_point_out, arithmetic_mean_point,
            geometric_median_point_out, geometric_median_point):
    # --- СРАВНЕНИЕ ---
    print("=== СДВИГ ОЦЕНОК ===")
    shift_mean = np.linalg.norm(arithmetic_mean_point_out - arithmetic_mean_point)
    shift_median = np.linalg.norm(geometric_median_point_out - geometric_median_point)

    print(f"Среднее сдвинулось на: {shift_mean:.4f}")
    print(f"Медиана сдвинулась на: {shift_median:.4f}")

