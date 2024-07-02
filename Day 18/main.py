from turtle import Turtle, Screen, colormode
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.color("blue")

# for x in range(10):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

colours = ["red", "blue", "green", "yellow", "black", "orange", "purple"]
colormode(255)


# for x in range(8):
#     num = 3+x
#     angle = 360/num
#     timmy.color(random.choice(colours))
#     for i in range(num):
#         timmy.forward(100)
#         timmy.right(angle)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)



# directions = ["left", "right"]

# timmy.pensize(10)
# timmy.speed(6)
# for x in range(100):
#     timmy.color(random_color())
#     res = random.choice(directions)
#     if res == "left":
#         timmy.left(90)
#         timmy.forward(30)
#     else:
#         timmy.right(90)
#         timmy.forward(30)


# Spirograph
timmy.speed("fastest")
for x in range(72):
    timmy.color(random_color())
    timmy.setheading(timmy.heading() + 5)
    timmy.circle(100)














screen = Screen()
screen.exitonclick()