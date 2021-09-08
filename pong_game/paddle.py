from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, xpos, ypos):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.shapesize(5, 1)
        self.penup()
        self.goto(xpos, ypos)

    def up(self):
        (x, y) = self.position()
        self.goto(x, y+20)

    def down(self):
        (x, y) = self.position()
        self.goto(x, y-20)
