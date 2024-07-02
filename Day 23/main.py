import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
car_list = []
scoreboard = Scoreboard()
counter = 0
speed = 0.1
frequency = 5



screen.listen()
screen.onkeypress(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(speed)
    screen.update()
    if player.ycor() >= 290:
        player.reset_player()
        scoreboard.update_scoreboard()
        speed -= 0.01
        if frequency != 2 and scoreboard.score%3 == 0:
            frequency -= 1
    if random.randint(1, frequency) == 1:
        car_list.append(CarManager())
    counter += 1
    for car in car_list:
        car.move_car()
        if player.distance(car) <= 20:
            game_is_on = False
        if car.xcor() < -350:
            car_list.remove(car)

scoreboard.game_over()







screen.exitonclick()
