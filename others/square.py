import turtle
turtle.bgcolor("black")

square = turtle.Turtle()
square.speed(20)
square.pencolor("blue")
for i in range(400):
    square.forward(i)
    square.left(91)