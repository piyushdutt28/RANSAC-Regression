from tracker import ObjectTracker

# Create a new object tracker
tracker = ObjectTracker(threshold=5, max_iterations=100)

# Add some positions to the tracker
tracker.add_position((10, 20))
tracker.add_position((20, 25))
tracker.add_position((30, 35))
tracker.add_position((40, 40))
tracker.add_position((50, 50))

# Get the filtered positions using RANSAC
filtered_positions = tracker.get_filtered_positions()

# Print the original positions and the filtered positions
print("Original positions:", tracker.positions)
print("Filtered positions:", filtered_positions)
