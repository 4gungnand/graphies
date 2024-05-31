import turtle

def draw_quadratic_bezier(A, B, C, num_points=100):
    # Set up the turtle
    turtle.speed(0)
    turtle.penup()

    # Move to the starting point
    turtle.goto(A)
    turtle.pendown()

    # Draw the curve
    for i in range(num_points):
        t = i / (num_points - 1)
        x = (1 - t) ** 2 * A[0] + 2 * (1 - t) * t * B[0] + t ** 2 * C[0]
        y = (1 - t) ** 2 * A[1] + 2 * (1 - t) * t * B[1] + t ** 2 * C[1]
        turtle.goto(x, y)

    # Reset the turtle
    turtle.penup()
    turtle.home()
    turtle.pendown()
p=200
q=150
# Define the control points

a = (-p,0)
b = (p,p)
c = (p,0)

draw_quadratic_bezier(a, b, c)

a = (-p,0)
b = (p,p)
c = (p,0)

A = (0, -200)
B = (-200, 100)
C = (0, 0)

# Wait for user to close window
turtle.done()
