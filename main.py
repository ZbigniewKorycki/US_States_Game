import turtle
import pandas as pd
from board import Board
from scoreboard import Scoreboard
import time

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states.gif"
turtle.addshape(image)
turtle.shape(image)

board = Board()
scoreboard = Scoreboard()

data = pd.read_csv("50_states.csv")

game_is_on = True
while game_is_on:
    time.sleep(0.01)
    screen.update()
    try:
        answer_state = screen.textinput(
            title=f"{scoreboard.get_score()} / {scoreboard.get_max_score()} States Correct",
            prompt="What's another state's name?",
        ).title()
    except AttributeError:
        states_to_learn = [
            state for state in list(data.state) if state not in board.recognized
        ]
        new_data = pd.DataFrame(states_to_learn)
        new_data.to_csv("states_to_learn.csv")
        game_is_on = False
    else:
        if answer_state == "Exit" or answer_state is None:
            states_to_learn = [
                state for state in list(data.state) if state not in board.recognized
            ]
            new_data = pd.DataFrame(states_to_learn)
            new_data.to_csv("states_to_learn.csv")
            game_is_on = False

        if answer_state in data.state.values:
            state_data = data[data.state == answer_state].iloc[0]
            board.create(x=int(state_data.x), y=int(state_data.y), name=answer_state)
            scoreboard.update()
        else:
            board.add_wrong(answer_state)

        if board.completed():
            scoreboard.finish()
            game_is_on = False