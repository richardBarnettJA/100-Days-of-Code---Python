from turtle import Turtle, Screen, colormode
import random
from colors import color_list
colormode(255)

dot = Turtle()
dot.pensize(15)
dot.speed("fastest")
dot.hideturtle()

y = - 280
for i in range(10):
    dot.penup()
    y += 50
    dot.setposition(-220, y)
    for x in range(10):
        dot.pendown()
        dot.color(random.choice(color_list))
        dot.begin_fill()
        dot.circle(5)
        dot.end_fill()
        dot.penup()
        dot.forward(50)





screen = Screen()
screen.exitonclick()



