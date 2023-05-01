import random
import numpy as np
from utils import calculate_distance

def ransac(data, threshold, max_iterations):
    """
    Use RANSAC to fit a line to the data and return the model and inliers.
    """
    best_model = None
    best_inliers = []
    for i in range(max_iterations):
        # Randomly sample two points from the data
        indices = random.sample(range(len(data)), 2)
        p1, p2 = data[indices[0]], data[indices[1]]
        
        # Calculate the line that passes through the two points
        dx, dy = p2[0] - p1[0], p2[1] - p1[1]
        if dx == 0:
            continue
        m = dy / dx
        b = p1[1] - m*p1[0]
        
        # Calculate the distance between each point and the line
        inliers = []
        for j, point in enumerate(data):
            d = abs(point[1] - m*point[0] - b) / np.sqrt(1 + m**2)
            if d < threshold:
                inliers.append(j)
        
        # If we have more inliers than the current best model, save the model and inliers
        if len(inliers) > len(best_inliers):
            best_model = (m, b)
            best_inliers = inliers
    
    return best_model, best_inliers
