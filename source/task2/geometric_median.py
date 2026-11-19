from source.common.gradient_descent import gradient_descent
import numpy as np


def make_f(points):
    def f(a):
        return np.sum(np.linalg.norm(points - a, axis=1))
    return f


def make_grad(points):
    def grad(a):
        diff = a - points
        dist = np.linalg.norm(diff, axis=1)
        dist = np.maximum(dist, 1e-12)
        return np.sum(diff / dist[:, None], axis=0)
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

    print(
        "БЕЗ ВЫБРОСА\n\n",
        "Арифметическое среднее: ",
        f"x = {arithmetic_mean_point[0]:.6f}, y = {arithmetic_mean_point[1]:.6f}, z = {arithmetic_mean_point[2]:.6f}, "
        f"F = {arithmetic_mean_value:.8f}\n",

        "Геометрическая медиана: ",
        f"x = {geometric_median_point[0]:.6f}, y = {geometric_median_point[1]:.6f}, z = {geometric_median_point[2]:.6f}, "
        f"F = {geometric_median_value:.8f}\n\n",

        f"Расстояние между ними: {np.linalg.norm(arithmetic_mean_point - geometric_median_point):.6f}\n",
        sep=""
    )

    return None



def print_result_with_outlier(
        arithmetic_mean_point_out, arithmetic_mean_value_out,
        geometric_median_point_out, geometric_median_value_out
):

    print(
        "С ВЫБРОСОМ\n\n",
        "Арифметическое среднее: ",
        f"x = {arithmetic_mean_point_out[0]:.6f}, y = {arithmetic_mean_point_out[1]:.6f}, z = {arithmetic_mean_point_out[2]:.6f}, "
        f"F = {arithmetic_mean_value_out:.8f}\n",

        "Геометрическая медиана: "
        f"x = {geometric_median_point_out[0]:.6f}, y = {geometric_median_point_out[1]:.6f}, z = {geometric_median_point_out[2]:.6f}, "
        f"F = {geometric_median_value_out:.8f}\n",

        sep="",
          )


def compare(arithmetic_mean_point_out, arithmetic_mean_point,
            geometric_median_point_out, geometric_median_point):

    shift_mean = np.linalg.norm(arithmetic_mean_point_out - arithmetic_mean_point)
    shift_median = np.linalg.norm(geometric_median_point_out - geometric_median_point)

    print("СДВИГ ОЦЕНОК\n\n",

    f"Среднее сдвинулось на: {shift_mean:.4f}\n",
    f"Медиана сдвинулась на: {shift_median:.4f}\n",

    sep="",
          )


def plot_results(points, points_out,
                 mean_pt, gm_pt,
                 mean_pt_out, gm_pt_out):
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D  # нужно для 3D
    import numpy as np

    fig = plt.figure(figsize=(14, 6))

    # БЕЗ ВЫБРОСА
    ax1 = fig.add_subplot(121, projection='3d')

    ax1.scatter(points[:, 0], points[:, 1], points[:, 2],
                c='blue', alpha=0.6, label='Точки (N=50)')

    ax1.scatter(*mean_pt, c='orange', marker='x', s=100,
                label='Среднее арифм.', linewidths=3)

    ax1.scatter(*gm_pt, c='green', marker='*', s=150,
                label='Геом. медиана')

    ax1.set_title('Без выброса')
    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    ax1.set_zlabel('Z')
    ax1.legend()

    # С ВЫБРОСОМ
    ax2 = fig.add_subplot(122, projection='3d')

    points_50 = points_out[:-1]
    outlier = points_out[-1]

    ax2.scatter(points_50[:, 0], points_50[:, 1], points_50[:, 2],
                c='blue', alpha=0.6, label='Точки (N=50)')

    ax2.scatter(*outlier, c='red', marker='D', s=80,
                label='Выброс (дист. 25)')

    ax2.scatter(*mean_pt_out, c='orange', marker='x', s=100,
                label='Среднее арифм.', linewidths=3)

    ax2.scatter(*gm_pt_out, c='green', marker='*', s=150,
                label='Геом. медиана')

    ax2.set_title('С выбросом')
    ax2.set_xlabel('X')
    ax2.set_ylabel('Y')
    ax2.set_zlabel('Z')
    ax2.legend()

    plt.tight_layout()

    plt.savefig('task2_results.png', dpi=300)

    plt.show()
