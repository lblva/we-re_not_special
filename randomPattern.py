import numpy as np
import cv2

# Define your base color palette (BGR format)
color_palette = np.array([
    (61, 170, 242),    # Blue
    (167, 217, 250),    # Light blue
    (40, 125, 181),    # Dark blue
    (255, 255, 133),  # Yellow
    (247, 232, 62),  # Orange
    (101, 184, 73),    # Green
    (146, 222, 150),    # Light green
    (53, 115, 56),    # Dark green
    (255, 130, 188),   # Pink
    (255, 122, 105),   # Light rood
    (252, 55, 30),   # Dark rood
    (250, 107, 243),   # Light purple
    (162, 41, 166)   # Dark purple
])

# Define pattern dimensions
pattern_height = 480
pattern_width = 640

# Create a blank canvas for the pattern with an alpha channel for transparency
pattern = np.zeros((pattern_height, pattern_width, 4), dtype=np.uint8)

# Set alpha channel to fully opaque (255)
pattern[:, :, 3] = 255

# Select a random background color from the color palette
bg_color_index = np.random.randint(0, len(color_palette))
bg_color = color_palette[bg_color_index]

# Fill the entire canvas with the selected background color
pattern[:, :, :3] = bg_color

# Select a random shape type
shape = np.random.choice(['rectangle', 'circle', 'line', 'zigzag'])

# Generate random shapes of the selected type with color from the color palette
color_index = np.random.randint(0, len(color_palette))
color = color_palette[color_index]
color = (int(color[0]), int(color[1]), int(color[2]))

if shape == 'rectangle':
    for _ in range(50):
        x, y, w, h = np.random.randint(0, pattern_width), np.random.randint(0, pattern_height), np.random.randint(20, 100), np.random.randint(20, 100)
        cv2.rectangle(pattern, (x, y), (x+w, y+h), color, -1)
elif shape == 'circle':
    for _ in range(50):
        center = np.random.randint(0, pattern_width), np.random.randint(0, pattern_height)
        radius = np.random.randint(10, 50)
        cv2.circle(pattern, center, radius, color, -1)
elif shape == 'line':
    for _ in range(50):
        start = np.random.randint(0, pattern_width), np.random.randint(0, pattern_height)
        end = np.random.randint(0, pattern_width), np.random.randint(0, pattern_height)
        cv2.line(pattern, start, end, color, np.random.randint(1, 5))
elif shape == 'zigzag':
    num_lines = 20
    line_spacing = pattern_height // num_lines
    for i in range(num_lines):
        points = np.array([[x, i * line_spacing] for x in range(0, pattern_width + 1, 20)], np.int32)
        cv2.polylines(pattern, [points], False, color, 5)

# Display the pattern
cv2.imshow('Colorful Pattern', pattern)
cv2.waitKey(0)
cv2.destroyAllWindows()
