import time
from turtle import Screen
from player import Player, STARTING_POSITION, MOVE_DISTANCE
from car_manager import CarManager, STARTING_MOVE_DISTANCE
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

player=Player()
car_manager=CarManager()
score=Scoreboard()

screen.onkey(key="Up", fun=player.moveForward)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    #detect collision  with the car
    for car in car_manager.cars:
        if player.distance(car)<20:
            score.game_over()
            game_is_on=False
    if player.ycor()>270:
        player.goto(STARTING_POSITION)
        car_manager.car_speed+=STARTING_MOVE_DISTANCE
        score.increase_score()

screen.exitonclick()