import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc, Polygon
import math
import random
import matplotlib.lines as lines


def rotate_point(x, y, angle, height):
    """Rotate a point (x, y) by the given angle in degrees."""
    angle_rad = math.radians(angle)
    x_rot = x * math.cos(angle_rad) - y * math.sin(angle_rad)
    y_rot = x * math.sin(angle_rad) + y * math.cos(angle_rad)
    return x_rot, y_rot

def plot_right_triangle(theta, rotation_angle=0, mirror=0, figname="test.pdf", target_index=1, source_index=0):
    # Create a figure and axis
    fig, ax = plt.subplots(figsize=(4, 4))

    base = math.cos(theta / (180.) * math.pi) * 4
    height = math.sin(theta / (180.) * math.pi) * 4

    centroid_x = base / 3.
    centroid_y = height / 3.

    print(base, height)

    # Coordinates of the triangle vertices based on the base and height
    A = [(-1)**mirror * (0    - centroid_x) , 0      - centroid_y]
    B = [(-1)**mirror * (base - centroid_x) , 0      - centroid_y]
    C = [(-1)**mirror * (0    - centroid_x) , height - centroid_y]

    A1 = [A[0], A[1]]
    A2 = [A[0], A[1] + 0.3]
    A3 = [A[0] + ((-1)**mirror * 0.3), A[1] + 0.3]
    A4 = [A[0] + ((-1)**mirror * 0.3), A[1]]

    # Rotate the triangle vertices
    A = rotate_point(*A, rotation_angle, height)
    B = rotate_point(*B, rotation_angle, height)
    C = rotate_point(*C, rotation_angle, height)

    A1 = rotate_point(*A1, rotation_angle, height)
    A2 = rotate_point(*A2, rotation_angle, height)
    A3 = rotate_point(*A3, rotation_angle, height)
    A4 = rotate_point(*A4, rotation_angle, height)

    # Highlight the target edge
    aa = [A, B]
    bb = [B, C]
    cc = [C, A]
    elements = [aa, bb, cc]
    edges = [elements[target_index], elements[source_index]]
    target = lines.Line2D([edges[0][0][0], edges[0][1][0]], [edges[0][0][1], edges[0][1][1]], color='red', linewidth=2)
    source = lines.Line2D([edges[1][0][0], edges[1][1][0]], [edges[1][0][1], edges[1][1][1]], color='blue', linewidth=2)
    ax.add_line(target)
    ax.add_line(source)

    # Plot the triangle
    triangle = plt.Polygon([A, B, C], fill=None, edgecolor='black')
    ax.add_patch(triangle)

    # Add an arc to represent the angle at vertex B
    angle = math.atan2(height, base) / (2. * math.pi) * 360
    angle_off_set = (180 - angle) * (mirror == 0) + rotation_angle
    base_radius = 0.4 * math.sqrt(base * height)
    angle_arc = Arc(B, width=base_radius, height=base_radius, angle=angle_off_set, theta1=0, theta2=angle, color='black', lw=0.7)
    ax.set_aspect('equal')
    ax.add_patch(angle_arc)

    # Right angle marker
    right_angle_marker = Polygon(
        [A1, A2, A3, A4],
        closed=True, edgecolor='black', facecolor='none', linewidth=0.7
    )
    ax.add_patch(right_angle_marker)

    # Label the sides
    # ax.text(base / 2, -0.4, 'a', fontsize=12, ha='center')  # Adjusted label for side 'a'
    # ax.text(-0.4, height / 2, 'b', fontsize=12, va='center')  # Adjusted label for side 'b'
    # ax.text(base / 2 - 0.3, height / 2 + 0.3, 'c', fontsize=12, ha='center')  # Adjusted label for side 'c'

    # Set the limits of the plot based on the triangle size

    coordinates = [A, B, C]
    x_values, y_values = zip(*coordinates)
    min_x = min(x_values)
    max_x = max(x_values)
    min_y = min(y_values)
    max_y = max(y_values)

    ax.set_xlim(min_x-0.1, max_x+0.1)
    ax.set_ylim(min_y-0.1, max_y+0.1)

    # Remove the axes
    ax.axis('off')

    # Display the plot
    plt.savefig(figname)

# 0 = adjc
# 1 = hypo
# 2 = oppo

# for i in range(100):
#     plot_right_triangle(theta=random.uniform(20, 80), rotation_angle=random.uniform(0, 360), mirror=random.randint(0, 1), figname=f"images/trig_{i}_ans1.png", target_index=0, source_index=1)
#     plot_right_triangle(theta=random.uniform(20, 80), rotation_angle=random.uniform(0, 360), mirror=random.randint(0, 1), figname=f"images/trig_{i}_ans2.png", target_index=0, source_index=2)
#     plot_right_triangle(theta=random.uniform(20, 80), rotation_angle=random.uniform(0, 360), mirror=random.randint(0, 1), figname=f"images/trig_{i}_ans3.png", target_index=1, source_index=0)
#     plot_right_triangle(theta=random.uniform(20, 80), rotation_angle=random.uniform(0, 360), mirror=random.randint(0, 1), figname=f"images/trig_{i}_ans4.png", target_index=1, source_index=2)
#     plot_right_triangle(theta=random.uniform(20, 80), rotation_angle=random.uniform(0, 360), mirror=random.randint(0, 1), figname=f"images/trig_{i}_ans5.png", target_index=2, source_index=0)
#     plot_right_triangle(theta=random.uniform(20, 80), rotation_angle=random.uniform(0, 360), mirror=random.randint(0, 1), figname=f"images/trig_{i}_ans6.png", target_index=2, source_index=1)

# for i in range(100):
#     plot_right_triangle(theta=random.uniform(20, 80), rotation_angle=0, mirror=random.randint(0, 1), figname=f"no_rotations/trig_{i}_ans1.png", target_index=0, source_index=1)
#     plot_right_triangle(theta=random.uniform(20, 80), rotation_angle=0, mirror=random.randint(0, 1), figname=f"no_rotations/trig_{i}_ans2.png", target_index=0, source_index=2)
#     plot_right_triangle(theta=random.uniform(20, 80), rotation_angle=0, mirror=random.randint(0, 1), figname=f"no_rotations/trig_{i}_ans3.png", target_index=1, source_index=0)
#     plot_right_triangle(theta=random.uniform(20, 80), rotation_angle=0, mirror=random.randint(0, 1), figname=f"no_rotations/trig_{i}_ans4.png", target_index=1, source_index=2)
#     plot_right_triangle(theta=random.uniform(20, 80), rotation_angle=0, mirror=random.randint(0, 1), figname=f"no_rotations/trig_{i}_ans5.png", target_index=2, source_index=0)
#     plot_right_triangle(theta=random.uniform(20, 80), rotation_angle=0, mirror=random.randint(0, 1), figname=f"no_rotations/trig_{i}_ans6.png", target_index=2, source_index=1)

plot_right_triangle(theta=30, rotation_angle=0, mirror=1, figname=f"material/trig_ans1.png", target_index=0, source_index=1)
plot_right_triangle(theta=30, rotation_angle=0, mirror=1, figname=f"material/trig_ans2.png", target_index=0, source_index=2)
plot_right_triangle(theta=30, rotation_angle=0, mirror=1, figname=f"material/trig_ans3.png", target_index=1, source_index=0)
plot_right_triangle(theta=30, rotation_angle=0, mirror=1, figname=f"material/trig_ans4.png", target_index=1, source_index=2)
plot_right_triangle(theta=30, rotation_angle=0, mirror=1, figname=f"material/trig_ans5.png", target_index=2, source_index=0)
plot_right_triangle(theta=30, rotation_angle=0, mirror=1, figname=f"material/trig_ans6.png", target_index=2, source_index=1)

# # Example usage with custom base and height
# for i in range(100):
#     plot_right_triangle(theta=random.uniform(20, 80), rotation_angle=random.uniform(0, 360), mirror=random.randint(0, 1), figname=f"test{i}.pdf")

