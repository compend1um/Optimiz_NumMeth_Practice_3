import numpy as np


def generate_points(quantity_of_points = 50):
    """
    :return: список, содержащий списки, состоящие из трех элементов - трех координат одной точки
    """
    np.random.seed(1) # зафиксировано зерно генерации

    points = np.random.rand(quantity_of_points, 3)
    return points


