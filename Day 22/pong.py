from turtle import Turtle, Screen
from paddles import Paddles
from center_line import Line
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


points = screen.numinput("Pong Game", "How many points would you like to play to?: ", 5, minval=1, maxval=100)


line = Line()
ball = Ball()
paddle_1 = Paddles("right")
paddle_2 = Paddles("left")
right_score = Scoreboard("right")
left_score = Scoreboard("left")



screen.listen()
screen.onkeypress(paddle_1.up, "Up")
screen.onkeypress(paddle_1.down, "Down")
screen.onkeypress(paddle_2.up, "w")
screen.onkeypress(paddle_2.down, "s")


speed = 0.1
counter = 0
is_game = True
while is_game:
    screen.update()
    time.sleep(speed)
    counter += 1
    if left_score.counter == points or right_score.counter == points:
        is_game = False
    else:
        if counter%200 == 0 and speed > 0.05:
            speed -= 0.01
            print(f"increase {speed}")
        if ball.xcor() > 340:
            # is_game = False
            left_score.add_score()
            ball.reset_position()
            speed = 0.1
        elif ball.xcor() < -340:
            # is_game = False
            right_score.add_score()
            ball.reset_position()
            speed = 0.1
        else:
            if ball.ycor() >= 280 or ball.ycor() <= -280:
                ball.bounce()
            

            if ball.xcor() > 330 and ball.distance(paddle_1)<50:
                ball.paddle_bounce()
            
            if ball.xcor() < -320 and ball.distance(paddle_2)<50:
                ball.paddle_bounce()

            ball.move()

left_score.game_over()




screen.exitonclick()