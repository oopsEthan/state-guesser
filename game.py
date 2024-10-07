from ui_handler import UI

class State_Guesser():
    def __init__(self) -> None:
        self.ui = UI()

        self.game_loop()

    def game_loop(self) -> None:
        self.ui.input_state()
    
    def run(self) -> None:
        self.ui.game_window.mainloop()