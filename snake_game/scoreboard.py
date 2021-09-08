from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Arial", 16, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.color('white')
        self.score = -1
        self.update_score()

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {(self.score)}", move=False,
                   align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", move=False,
                   align=ALIGNMENT, font=FONT)
