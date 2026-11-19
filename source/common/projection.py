import numpy as np
from math import sqrt

def projection_circle(point, radius=sqrt(7)):
    point = np.array(point)
    position = np.linalg.norm(point)

    if position <= radius:
        return point

    return point * (radius / position)
