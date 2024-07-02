from turtle import Turtle

UP = 90
DOWN = 270

class Paddles(Turtle):
    def __init__(self, side):
        super().__init__()
        self.shape("square")
        self.shapesize(5, 1)
        self.color("white")
        self.penup()
        self.speed("fastest")
        if side =="right":
            self.goto(350, 0)
        elif side == "left":
            self.goto(-350, 0)
    
    def up(self):
        if self.ycor() <= 240:
            y = self.ycor() + 20
            self.goto(self.xcor(), y)

    def down(self):
        if self.ycor() >= -240:
            y = self.ycor() - 20
            self.goto(self.xcor(), y)