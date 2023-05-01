import numpy as np

def calculate_distance(p1, p2):
    """
    Calculate the Euclidean distance between two points in 2D space.
    """
    return np.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)
