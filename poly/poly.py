# Take user input txt pattern and display the polyhedron
import turtle
import time
import random

num_str = input("Enter the side number of the shape you want to draw: ")
if num_str.isdigit():
	squares = int(num_str)

angle = 180 - 180*(squares-2)/squares

turtle.up

x = 0
y = 0
turtle.setpos(x, y)


num_shapes = 8
for x in range(num_shapes):
	turtle.color(random.random(), random.random(), random.random())
	x += 5
	y += 5
	turtle.forward(x)
	turtle.left(y)
	for i in range(squares):
		turtle.begin_fill()
		turtle.down()
		turtle.forward(40)
		turtle.left(angle)
		turtle.forward(40)
		print (turtle.pos())
		turtle.up()
		turtle.end_fill()

time.sleep(11)
turtle.bye()
