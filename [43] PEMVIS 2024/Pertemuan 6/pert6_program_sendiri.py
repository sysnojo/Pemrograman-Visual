# Generating a Unique Abstract Illustration

import numpy as np
import matplotlib.pyplot as plt

# Define canvas dimensions
canvas_width = 1500
canvas_height = 1500

# Define parameters for the abstract shapes
num_shapes = 20
max_radius = 300

# Create a canvas
canvas = np.zeros(shape=(canvas_height+1, canvas_width+1, 3), dtype=np.int16)

# Generate random shapes on the canvas
for _ in range(num_shapes):
    # Random center coordinates
    center_x = np.random.randint(max_radius, canvas_width - max_radius)
    center_y = np.random.randint(max_radius, canvas_height - max_radius)
    
    # Random radius
    radius = np.random.randint(50, max_radius)
    
    # Random color
    color = np.random.randint(0, 256, size=3)
    
    # Draw the shape on the canvas
    for y in range(center_y - radius, center_y + radius):
        for x in range(center_x - radius, center_x + radius):
            if (x - center_x)**2 + (y - center_y)**2 <= radius**2:
                canvas[y, x] = color

# Display the unique abstract illustration
plt.figure(figsize=(8, 8))
plt.imshow(canvas)
plt.axis('off')
plt.show()
