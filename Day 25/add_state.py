from turtle import Turtle

class Add_State(Turtle):
    def __init__(self, x, y, state):
        super().__init__()
        self.x = x
        self.y = y
        self.state = state
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.goto(self.x, self.y)
        self.write(self.state)