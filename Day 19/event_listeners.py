from turtle import Turtle, Screen


tim = Turtle()

def move_up():
        tim.forward(50)

def move_back():
        tim.backward(50)

def turn_left():
    tim.setheading(tim.heading() + 10)

def turn_right():
    tim.setheading(tim.heading() - 10)

def clear_screen():
      tim.clear()
      tim.penup()
      tim.home()
      tim.pendown()
    



screen = Screen()
screen.listen()
screen.onkey(move_up, "w")
screen.onkey(move_back, "s")
screen.onkey(turn_right, "d")
screen.onkey(turn_left, "a")
screen.onkey(clear_screen, "c")
screen.exitonclick()

