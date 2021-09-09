from turtle import Turtle
import pandas
STATES = 'us_states_game/50_states.csv'
FONT = ("Arial", 10, "normal")


class Mapper(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.STATES_COORD = Mapper.read_states()

    def print_on_map(self, state):
        self.goto(self.STATES_COORD[state])
        self.write(state, move=False,
                   align="center", font=FONT)

    def valid_state(self, state):
        return state in self.STATES_COORD

    def read_states():
        data = pandas.read_csv(STATES)
        states = data.state
        x = data.x
        y = data.y
        return {states[i]: (x[i], y[i]) for i in range(len(states))}
