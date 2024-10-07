from turtle import *
from pandas import *

SCREEN_X = 900
SCREEN_Y = 590
BACKGROUND_IMAGE = "usa_map.gif"

class UI(Turtle):
    def __init__(self) -> None:
        super().__init__()
        
        self.game_window = Screen()
        self.game_window.bgpic(BACKGROUND_IMAGE)
        self.game_window.setup(SCREEN_X, SCREEN_Y)

        self.guessed_states = []

        self.state_information = read_csv("usa_states_data.csv")
        self.hideturtle()

    def draw_state(self, state_name) -> None:
        if state_name not in self.guessed_states:
            state_id = self.state_information[self.state_information.state == state_name]
            state_x = int(state_id.state_x)
            state_y = int(state_id.state_y)

            self.teleport(state_x, state_y)
            self.write(f"{state_name}", align="center", font=("Courier", 10, "normal"))