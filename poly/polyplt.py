import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

alpha = 55
beta = 25
Distance = 10

# Define the vertices of the pyramid
vertex = [
    [0, 0, 0],
    [2, 0, 0],
    [2, 0, 2],
    [0, 0, 2],
    [0.5, 4, 0.5],
    [1.5, 4, 0.5],
    [1.5, 4, 1.5],
    [0.5, 4, 1.5],
    [0.5, 5, 0.5],
    [1.5, 5, 0.5],
    [1.5, 5, 1.5],
    [0.5, 5, 1.5],
    [0.5, 6, 0.5],
    [1.5, 6, 0.5],
    [1.5, 6, 1.5],
    [0.5, 6, 1.5]
]

# Define the faces of the pyramid
faces = [
    [1, 2, 6, 5],
    [1, 4, 8, 5],
    [2, 3, 7, 6],
    [5, 6, 7, 8],
    [3, 4, 8, 7],
    [1, 2, 3, 4],
    [9, 10, 14, 13],
    [9, 12, 16, 13],
    [10, 11, 15, 14],
    [13, 14, 15, 16],
    [11, 12, 16, 15],
    [9, 10, 11, 12]
]

# Calculate the average z-coordinate for each face
avg_z = [sum(vertex[i - 1][2] for i in face) / len(face) for face in faces]

# Sort the faces based on average z-coordinate
faces_sorted = [face for _, face in sorted(zip(avg_z, faces))]

# Create a new figure and axes
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Draw the pyramid
for face in faces_sorted:
    vertices = [vertex[i - 1] for i in face]  # Subtract 1 from each vertex index
    ax.add_collection3d(Poly3DCollection([vertices], facecolors=(0.1, 0.2, 0.5, 0.3), edgecolors='black'))

# Set the axis limits
ax.set_xlim([0, 2])
ax.set_ylim([0, 6])
ax.set_zlim([0, 2])

# Set the viewing angle
ax.view_init(alpha, beta)

# Show the plot
plt.show()
