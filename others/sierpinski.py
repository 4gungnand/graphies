import turtle

N = 200

a, b, c, d, e, f = [0]*3, [0]*3, [0]*3, [0]*3, [0]*3, [0]*3

# Transformation 1
a[0] = 0.5; b[0] = 0; c[0] = 0; d[0] = 0.5; e[0] = 0; f[0] = 0
# Transformation 2
a[1] = 0.5; b[1] = 0; c[1] = 0; d[1] = 0.5; e[1] = 0; f[1] = N/2
# Transformation 3
a[2] = 0.5; b[2] = 0; c[2] = 0; d[2] = 0.5; e[2] = N/2; f[2] = 0

def affineTransform(point):
    x = point[0]
    y = point[1]

    # Affine Transformation
    points = []
    for i in range(3):
        point = [0, 0]
        point[0] = a[i]*x + b[i]*y + e[i]
        point[1] = c[i]*x + d[i]*y + f[i]
        points.append(point)
    return points

def drawObject(points, color, myTurtle):
    # myTurtle.fillcolor(color)
    myTurtle.up()
    myTurtle.goto(points[0][0], points[0][1])
    myTurtle.down()
    # myTurtle.begin_fill()
    myTurtle.goto(points[1][0], points[1][1])
    myTurtle.goto(points[2][0], points[2][1])
    myTurtle.goto(points[0][0], points[0][1])
    # myTurtle.end_fill()


def sierpinski(points, degree, myTurtle):
    colormap = ['blue', 'red', 'green', 'white', 'yellow',
                'violet', 'orange']

    drawObject(points,colormap[degree],myTurtle)

    if degree > 0:
        ob1 = affineTransform(points[0])
        ob2 = affineTransform(points[1])
        ob3 = affineTransform(points[2])
        sierpinski([ob1[0],ob2[0],ob3[0]],degree-1, myTurtle)
        sierpinski([ob1[1],ob2[1],ob3[1]],degree-1, myTurtle)
        sierpinski([ob1[2],ob2[2],ob3[2]],degree-1, myTurtle)

def main():
   myTurtle = turtle.Turtle()
   myWin = turtle.Screen()
   myPoints = [[0,0],[0,N],[N,0]]
   sierpinski(myPoints,5,myTurtle)
   myWin.exitonclick()
    

main()