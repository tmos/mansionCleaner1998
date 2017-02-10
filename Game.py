import Mansion
import Robot


class Game:
    """
    Main class for the mansion cleaning game.
    """
    instance = None
    mansion = None
    robot = None

    "Game"
    def __init__(self):
        if not self.instance:
            self.instance = self

    def get_game(self):
        if not self.instance:
            self.__init__()

        return self.instance

    "Mansion"
    def get_current_mansion(self):
        if not self.mansion:
            self.create_new_mansion()

        return self.mansion

    def create_new_mansion(self):
        self.mansion = Mansion.Mansion()

    "Robot"
    def create_new_robot(self, mansion):
        self.robot = Robot.Robot(mansion)
        return self.robot

    def get_robot(self):
        if not self.robot:
            if not self.mansion:
                self.create_new_mansion()
            self.create_new_robot(self.mansion)

        return self.robot

    def start_robot(self):
        self.robot.live()
