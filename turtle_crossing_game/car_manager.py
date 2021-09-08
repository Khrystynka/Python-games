from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
Y_POSITIONS = (-200, 200)


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        dice = random.randint(1, 6)
        if dice == 1:
            y_pos = random.randint(*Y_POSITIONS)
            self.cars.append(Car(y_pos))

    def move(self):
        for car in self.cars:
            car.backward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT


class Car(Turtle):
    def __init__(self, ypos):
        super().__init__()
        self.color(random.choice(COLORS))
        self.shape('square')
        self.shapesize(1, 2)
        self.penup()
        self.goto(300, ypos)

        # self.setheading(180)
