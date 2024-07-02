from turtle import Turtle

FONT = ("Courier", 24, "normal")
FONT2 = ("Courier", 25, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-270, 230)
        self.score = 1
        self.write_scoreboard()

    def write_scoreboard(self):
        self.write(f"Level: {self.score}", font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.score += 1
        self.write_scoreboard()

    def game_over(self):
        self.color("red")
        self.goto(0, 0)
        self.write("GAME OVER!", align="center", font=FONT2)

