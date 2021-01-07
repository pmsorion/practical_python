from turtle import *
import turtle

window = turtle.Screen()
setup(250, 250, 0, 0)
screensize(120, 120)
colormode(255)
hideturtle()

penup()
goto(0,80)
dot(40, 0, 0, 255)
goto(0, 40)
dot(40, 255, 0, 0)
goto(0, 0)
dot(40, 0, 0, 0)
goto(0, -40)
dot(40, 0, 255, 0)
goto(0, -80)
dot(40, 255, 0, 255)


window.mainloop()