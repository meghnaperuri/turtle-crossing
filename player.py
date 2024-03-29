from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.createPlayer()

    def createPlayer(self):
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def moveForward(self):
        self.forward(MOVE_DISTANCE)
