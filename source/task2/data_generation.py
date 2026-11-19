import numpy as np


def generate_points(quantity_of_points = 50):
    """
    :return: список, содержащий списки, состоящие из трех элементов - трех координат одной точки
    """
    np.random.seed(1)

    points = np.random.rand(quantity_of_points, 3)
    return points


def add_outlier(points, distance=25.0):

    center = np.array([0.5, 0.5, 0.5])

    rng = np.random.default_rng(42)
    direction = rng.normal(size=3)
    direction /= np.linalg.norm(direction)

    outlier = center + distance * direction

    return np.vstack([points, outlier])



