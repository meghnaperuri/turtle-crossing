from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.create_turtle()
        self.create_score()
    def create_turtle(self):
        self.penup()
        self.hideturtle()
        self.color("white")
    def create_score(self):
        self.goto(-20,270)
        self.write("score: "+str(self.score),font=FONT)
    def increase_score(self):

        self.clear()
        self.score+=1
        self.create_score()
    def game_over(self):
        self.create_turtle()
        self.goto(-20,0)
        self.write("game over.",font=FONT)



