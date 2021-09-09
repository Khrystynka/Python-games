import turtle

import pandas
from pandas.core.frame import DataFrame
import mapper
MAP = 'us_states_game/blank_states_img.gif'

screen = turtle.Screen()
screen.addshape(MAP)
map = turtle.Turtle()
map.shape(MAP)
correct_answers = 0
game_on = True
guessed = set()
not_guessed = []
mapper = mapper.Mapper()
while game_on:
    user_guess = screen.textinput(
        title=f"{correct_answers}/50 Correct answers", prompt="Please type your next guess: ").title()
    print(user_guess)
    if user_guess == "Exit":
        for state in mapper.STATES_COORD:
            if state not in guessed:
                not_guessed.append(state)
        data = DataFrame(not_guessed)
        data.to_csv('us_states_game/states_to_learn')
        break
    if mapper.valid_state(user_guess) and user_guess not in guessed:
        correct_answers += 1
        mapper.print_on_map(user_guess)
        guessed.add(user_guess)


# def get_mouse_click_coor(x, y):
#     print(x, y)


# turtle.onscreenclick(get_mouse_click_coor)

# turtle.mainloop()

screen.exitonclick()
