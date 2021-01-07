import turtle
from turtle import *

window = turtle.Screen()
setup(250, 250, 0, 0)
screensize(120, 120)
hideturtle()

penup()
goto(-100, 0)
pendown()
goto(-50, 50)
goto(50, -50)
goto(100, 0)
goto(50, 50)
goto(-50, -50)
goto(-100, 0)

penup()
goto(0, 50)
dot(50, 0, 0, 0)
goto(0, -50)
dot(50, 0, 0, 0)

window.mainloop()