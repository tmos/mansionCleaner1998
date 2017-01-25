import Mansion
import Robot

class Game:
    """
    Main class for the mansion cleaning game.
    """
    instance = None
    current_mansion = None

    def __init__(self):
        if not self.instance:
            Game.instance = self

    def get_game(self):
        if not self.instance:
            self.__init__()

        return self.instance

    def get_current_mansion(self):
        if not self.current_mansion:
            self.create_new_mansion()

        return self.current_mansion

    def create_new_mansion(self):
        self.current_mansion = Mansion.Mansion()

G = Game()
m = G.get_current_mansion()
m.print_mansion()
