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
        self.pen(shown=False, pencolor="red")
    
    def input_state(self) -> None:
        while len(self.guessed_states) < 50:
            guess = self.game_window.textinput("Guess a State.", f"{len(self.guessed_states)}/50 States guessed!")
            if guess not in self.guessed_states and guess != None:
                 guess = guess.title().replace(" ", "_")
                 print(f"Guess is: {guess}")
                 self.draw_state(guess)

    def draw_state(self, state_name) -> None:
            state_id = self.state_information[self.state_information.state == state_name]
            if state_id.empty:
                 return
            state_x = state_id.state_x.values[0]
            state_y = state_id.state_y.values[0]

            self.teleport(state_x, state_y)
            self.guessed_states.append(state_name)
            state_name = state_name.replace("_"," ")
            self.write(f"{state_name}", align="center", font=("Courier", 12, "normal"))