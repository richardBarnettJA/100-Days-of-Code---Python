from turtle import Turtle, Screen, TK, write
import random

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

turtles = []

for x in range(6):
    t = Turtle(shape="turtle")
    t.color(colors[x])
    turtles.append(t)


finish = Turtle()
finish.hideturtle()
finish.speed("fastest")
finish.pensize(15)
finish.penup()
finish.setposition(-250, 190)
finish.pendown()
finish.forward(500)
finish.penup()
finish.setposition(-50, 145)
finish.write("FINISH", font=("Verdana",
                                    25, "normal"))
finish.penup()
finish.setposition(-250, 140)
finish.pendown()
finish.forward(500)
finish.penup()
finish.setposition(-250, -140)
finish.pendown()
finish.forward(500)




screen = Screen()
screen.setup(width=500, height=400)





val = -100
for i in turtles:
    val += 30
    i.penup()
    i.setheading(90)
    i.goto(x = val , y = -170)

user_bet = screen.textinput(title = "Make your bet!", prompt="Which turtle will win the race? Enter a color: ")

winner = ""
is_game = True
while is_game:
    t = random.choice(turtles)
    t.forward(random.randint(0, 10))
    if t.ycor() >= 160:
        is_game = False
        winner = t.pencolor()


if winner.lower() == user_bet.lower():
    message = TK.messagebox.showinfo(title="Results", message=f"YOU WON! You bet {winner} correctly!!!")
else:
    message = TK.messagebox.showinfo(title="Results", message=f"You lost! You bet incorrectly. The race was won by {winner}.")
if message == "ok":
    screen.bye()
screen.exitonclick()