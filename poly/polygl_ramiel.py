"program that tries to display Ramiel (Evangelion) using OpenGL"

# How to run: python poly/polygl.py pyramid.txt

import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
import sys
import math

class Polyhedron:
    
    def __init__(self, vertices, faces):
        self.vertices = vertices
        self.faces = faces
        
    def draw(self, color):        
        glBegin(GL_QUADS)
        for face in self.faces:
            glColor3fv(color)
            for vertex_index in face:
                vertex = self.vertices[vertex_index-1]
                glVertex3fv(vertex)
        glEnd()

    def draw_edges(self):
        glColor3f(0, 0, 0)  # Set edge color to black
        glLineWidth(2.0)  # Set line width
        for face in self.faces:
            glBegin(GL_LINE_LOOP)
            for vertex_index in face:
                vertex = self.vertices[vertex_index-1]
                glVertex3fv(vertex)
            glEnd()

    @staticmethod
    def from_text_file(filename):
        rows, cols, vertices, faces = Polyhedron.parse_text_file(filename)
        return Polyhedron(vertices, faces)

    @staticmethod
    def parse_text_file(filename):
        try:
            with open(filename, 'r') as file:
                content = file.read()
            
            lines = content.splitlines()
            rows, cols = map(int, lines[0].split())
            
            vertices = []
            for line in lines[1:rows+1]:
                vertex = list(map(float, line.split()))
                vertices.append(vertex)
            
            faces = []
            for line in lines[rows+1:]:
                face = list(map(int, line.split()))
                face.pop(0)
                faces.append(face)
            
            return rows, cols, vertices, faces

        except IOError:
            print(f"Error: Unable to read file '{filename}'.")

    def __str__(self):
        return f"Polyhedron(\nvertices={self.vertices}, \nfaces={self.faces}), \nvertices={len(self.vertices)},\nfaces={len(self.faces)}\n)"

def draw_sphere(radius, slices, stacks):
    for i in range(slices):
        lat0 = math.pi * (-0.5 + float(i) / slices)
        z0 = math.sin(lat0)
        zr0 = math.cos(lat0)

        lat1 = math.pi * (-0.5 + float(i + 1) / slices)
        z1 = math.sin(lat1)
        zr1 = math.cos(lat1)

        glBegin(GL_QUAD_STRIP)
        for j in range(stacks + 1):
            lng = 2 * math.pi * float(j) / stacks
            x = math.cos(lng)
            y = math.sin(lng)

            glNormal3f(x * zr0, y * zr0, z0)
            glVertex3f(x * zr0 * radius, y * zr0 * radius, z0 * radius)
            glNormal3f(x * zr1, y * zr1, z1)
            glVertex3f(x * zr1 * radius, y * zr1 * radius, z1 * radius)
        glEnd()

def draw_torus(color1, color2):
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        poly = Polyhedron.from_text_file(filename)
    else:
        print("Error: No file name provided.")
        sys.exit(1)

    angle = pygame.time.get_ticks() * 0.1  # Get a continuously changing angle

    glPushMatrix()
    glTranslatef(0, -.25, 0)  # Translate down
    glRotatef(angle, 0, 1, 0)  # Rotate counter-clockwise around y-axis
    glScalef(1, -1, 1)  # Flip in the y direction
    poly.draw(color1)
    poly.draw_edges()
    glPopMatrix()

    glPushMatrix()
    glColor3f(1, 0, 0)  # Set color to red
    draw_sphere(0.05, 20, 20)  # Draw sphere with radius 0.05
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0, .25, 0)  # Translate up
    glRotatef(-angle, 0, 1, 0)  # Rotate clockwise around y-axis
    poly.draw(color2)
    poly.draw_edges()
    glPopMatrix()

def main():
    global surfaces

    pygame.init()
    display = (800, 600)
    screen = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    clock = pygame.time.Clock()

    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

    glMatrixMode(GL_MODELVIEW)
    glTranslatef(0, 0, -5)
    
    glClearColor(0.5, 0.5, 0.5, 0.0)

    glLight(GL_LIGHT0, GL_POSITION, (5, 5, 5, 1))  # point light from the left, top, front
    glLightfv(GL_LIGHT0, GL_AMBIENT, (0, 0, 0, 1))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (1, 1, 1, 1))

    glEnable(GL_DEPTH_TEST)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glEnable(GL_COLOR_MATERIAL)
        glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

        draw_torus((0, 0, 1), (0, 0, 0.5))  # Draw pyramids

        glDisable(GL_LIGHT0)
        glDisable(GL_LIGHTING)
        glDisable(GL_COLOR_MATERIAL)

        pygame.display.flip()
        clock.tick(60)

main()