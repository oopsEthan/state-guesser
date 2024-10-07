from ui_handler import UI

class State_Guesser():
    def __init__(self) -> None:
        self.ui = UI()
    
    def run(self) -> None:
        self.ui.game_window.mainloop()