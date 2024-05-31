from turtle import *

RAD = 100
RAD2 = RAD / 2
RAD6 = RAD / 6

speed(1)
hideturtle()

degrees() # Switch to degrees
# Draw the circle, radius 100, half black
fillcolor('black')
circle(RAD, 90)
begin_fill()
circle(RAD, 180)
end_fill()
circle(RAD, 90)

# Draw smaller black semi-circle
right(90)
penup()
goto(0, RAD)
pendown()
begin_fill()
circle(RAD2, 180)
end_fill()

# Draw smaller white semi-circle
penup()
goto(0, RAD)
pendown()
fillcolor('white')
begin_fill()
circle(RAD2, 180)
end_fill()

end_fill()
exitonclick()