import turtle
import random

POSITIONS = [(20, 0), (0, 0), (-20, 0)]
# COLORS = ['green', 'blue', 'white',
#           'yellow', 'orange', 'purple', 'red']
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):

        self.snake = []
        for position in POSITIONS:
            self.snake.append(self.create_segment(position))
        self.head = self.snake[0]

    def create_segment(self, position):

        new_segment = turtle.Turtle('square')
        new_segment.penup()
        new_segment.color('white')
        new_segment.goto(position)
        return new_segment

    def expand_snake(self):
        self.snake.append(self.create_segment(self.snake[-1].position()))

    def move(self):
        for i in range(len(self.snake)-1, 0, -1):
            self.snake[i].goto(self.snake[i-1].xcor(), self.snake[i-1].ycor())
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
