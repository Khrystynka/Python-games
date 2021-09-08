from turtle import Turtle
import time


class Ball(Turtle):
    def __init__(self, screenx, screeny):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):

        new_xcor = self.xcor() + self.x_move
        new_ycor = self.ycor() + self.y_move
        self.goto(new_xcor, new_ycor)

    def y_bounce(self):
        self.y_move *= -1

    def x_bounce(self):
        self.x_move *= -1

    def new_round(self):
        self.goto(0, 0)
        self.x_bounce()
