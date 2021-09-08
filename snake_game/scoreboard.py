from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Arial", 16, "normal")
DATA = 'snake_game/data.txt'


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.color('white')
        self.score = 0
        with open(DATA) as file:
            self.highest_score = int(file.read())
            print(self.highest_score)
        self.reset()

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {(self.score)} Highest score: {self.highest_score}", move=False,
                   align=ALIGNMENT, font=FONT)

    def reset(self):
        self.clear()
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open(DATA, 'w') as file:
                file.write(str(self.highest_score))
        self.score = 0
        self.write(f"Score: {(self.score)} Highest score: {self.highest_score}", move=False,
                   align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", move=False,
                   align=ALIGNMENT, font=FONT)
