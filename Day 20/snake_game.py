from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

SPEED = 0.1

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# snake = Turtle("square")
# snake.color("white")
# snake.shapesize(1, 6, 1)


sn = Snake()
fd = Food()
sc = Scoreboard()
sc.add_score()



screen.listen()
screen.onkey(sn.up, "Up")
screen.onkey(sn.down, "Down")
screen.onkey(sn.left, "Left")
screen.onkey(sn.right, "Right")


screen.update()

is_game = True
while is_game:
    screen.update()
    time.sleep(SPEED)
    sn.move()
    if sn.head.ycor() >= 300 or sn.head.ycor() <= -300 or sn.head.xcor() >= 300 or sn.head.xcor() <= -300:
        # is_game = False
        # sc.game_over()
        sc.reset()
        sn.reset()
    if sn.head.distance(fd) < 20:
        sc.add_score()
        sn.grow()
        fd.refresh()
    for s in sn.snake_body[1:]:
        if sn.head.distance(s) < 10:
            # is_game = False
            # sc.game_over()
            sc.reset()
            sn.reset()






screen.exitonclick()