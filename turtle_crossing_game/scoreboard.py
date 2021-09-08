from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-200, 250)
        self.level = 1
        self.hideturtle()
        self.color('black')
        self.update_level()

    def update_level(self):
        self.clear()

        text = "LEVEL: " + str(self.level)
        self.write(text, align='Center', font=FONT)

    def game_over(self):
        self.goto(0, 0)

        self.write("GAME OVER!", align='Center', font=FONT)
