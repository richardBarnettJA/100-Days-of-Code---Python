from turtle import Turtle

class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, -285)
        self.hideturtle()
        self.pensize(10)
        self.setheading(90)
        self.draw_line()

    def draw_line(self):
        for x in range(12):
            self.pendown()
            self.forward(25)
            self.penup()
            self.forward(25)