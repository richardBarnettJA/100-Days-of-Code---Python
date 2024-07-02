from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("orange")
        self.shape("circle")
        self.penup()
        self.setheading(45)
        self.y_move = 10
        self.x_move = 10

    def move(self):
        y = self.ycor() + self.y_move
        x = self.xcor() + self.x_move
        self.goto(x, y)


    def bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.paddle_bounce()
        
            