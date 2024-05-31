from math import cos, sin, pi
from PIL import Image, ImageDraw

# Definisikan parameter transformasi
alpha = -20
beta = -20
Distance = 10
L = 800
T = 700

# Definisikan vertex dan faces
vertex = [[0, 5, 0], [-2, 0, 2], [2, 0, 2], [2, 0, -2], [-2, 0, -2]]
faces = [[0, 1, 2], [0, 2, 3], [0, 3, 4], [0, 4, 1], [1, 2, 3, 4]]

# Definisikan a fungsi untuk transformasi koordinat 3D ke koordinat 2D 
def transform(x, y, z):
    # Apply rotation
    xs = -z*sin(alpha/180) + x*cos(alpha/180)
    ys = -z*cos(alpha/180)*sin(beta/180) - x*sin(alpha/180)*sin(beta/180) + y*cos(beta/180)
    zs = Distance - (-z*cos(alpha/180)*cos(beta/180) - x*sin(alpha/180)*cos(beta/180) - y*sin(beta/180))
    # Apply projection
    xp = (xs*L/2)/zs
    yp = (ys*L/2)/zs
    # Translate to screen coordinates
    xd = L/2 + round(xp)
    yd = T/2 - round(yp)
    return xd, yd

img = Image.new('RGB', (L, T), 'white')
draw = ImageDraw.Draw(img)
for face in faces:
    points = []
    for vertex_index in face:
        x, y, z = vertex[vertex_index]
        points.append(transform(x, y, z))
    draw.polygon(points, fill='gray', outline='black')

# Simpan gambar
img.save('pyramid.png')