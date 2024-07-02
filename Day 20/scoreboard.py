from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.counter = -1
        self.high_score = int(self.get_high_score())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_score()
        self.update_high_score()

    def update_score(self):
        self.goto(-100, 260)
        self.write(f"Score: {self.counter}", align="center", font=("Arial", 24, "normal"))

    def update_high_score(self):
        self.goto(100, 260)
        self.write(f"High Score: {self.high_score}", align="center", font=("Arial", 24, "normal"))

    def add_score(self):
        self.counter += 1
        if self.counter > self.high_score:
            self.high_score = self.counter
            with open("data.txt", "w") as f:
                f.write(str(self.high_score))
        self.clear()
        self.update_score()
        self.update_high_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!", align="center", font=("Arial", 30, "normal"))

    def reset(self):
        self.counter = 0
        self.clear()
        self.update_score()
        self.update_high_score()

    def get_high_score(self):
        with open("data.txt", "r") as f:
            return f.read()
