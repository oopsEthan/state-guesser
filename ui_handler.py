from turtle import *

SCREEN_X = 900
SCREEN_Y = 590
BACKGROUND_IMAGE = "usa_map.gif"

class UI(Turtle):
    def __init__(self) -> None:
        super().__init__()
    game_screen = Screen()
    game_screen.bgpic(BACKGROUND_IMAGE)
    game_screen.setup(SCREEN_X, SCREEN_Y)

    game_screen.mainloop()