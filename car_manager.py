from turtle import Turtle, Screen
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

screen = Screen()


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed=STARTING_MOVE_DISTANCE
    def create_car(self):
        random_chance=random.randint(1,6)
        if random_chance==1:
            print(random_chance)
            new_car=Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y=random.randint(-250,250)
            new_car.left(90)
            new_car.goto(300,random_y)
            self.cars.append(new_car)
    def move_cars(self):
        for car in self.cars:
            car.setheading(180)
            car.forward(self.car_speed)

    def update(self):
        self.move_cars()