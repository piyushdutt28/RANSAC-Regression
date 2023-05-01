from utils import calculate_distance
from ransac import ransac

class ObjectTracker:
    """
    A simple object tracker that uses RANSAC to remove noise from position data.
    """
    
    def __init__(self, threshold=5, max_iterations=100):
        self.threshold = threshold
        self.max_iterations = max_iterations
        self.positions = []
    
    def add_position(self, position):
        """
        Add a new position to the tracker.
        """
        self.positions.append(position)
    
    def get_filtered_positions(self):
        """
        Use RANSAC to remove noise from the positions and return the filtered positions.
        """
        filtered_positions = []
        if len(self.positions) > 2:
            model, inliers = ransac(self.positions, self.threshold, self.max_iterations)
            for i in inliers:
                filtered_positions.append(self.positions[i])
        return filtered_positions
