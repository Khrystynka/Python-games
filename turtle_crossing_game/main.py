import turtle
from player import Player
import time
import random
from car_manager import CarManager
from scoreboard import Scoreboard


screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.title('TURTLE CROSSING')

screen.tracer(0)

game_on = True

scoreboard = Scoreboard()


screen.listen()
sleep = 0.1
player = Player()
cars = CarManager()

screen.onkey(player.up, "Up")


while game_on:
    screen.update()
    time.sleep(sleep)
    cars.create_car()
    cars.move()

    if player.ycor() > 280:
        player.reset_position()
        cars.increase_speed()
        scoreboard.update_level()
    for car in cars.cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_on = False


screen.exitonclick()
