from turtle import Turtle
INITIAL_POSITION = (0, -280)


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.penup()
        self.reset_position()
        self.level = 1

    def reset_position(self):
        self.goto(INITIAL_POSITION)
        self.setheading(90)

    def up(self):
        self.goto(self.xcor(), self.ycor()+10)
