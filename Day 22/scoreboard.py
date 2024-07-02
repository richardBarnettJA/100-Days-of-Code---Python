from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, side):
        super().__init__()
        self.counter = 0
        self.color("white")
        self.penup()
        if side == "right":
            self.setposition(60, 150)
        elif side == "left":
            self.setposition(-60, 150)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"{self.counter}", align="center", font=("Arial", 100, "normal"))


    def add_score(self):
        self.counter += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, -50)
        self.color("red")
        self.write(f"GAME OVER!", align="center", font=("Arial", 60, "normal"))