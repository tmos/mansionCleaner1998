import Game
import os
import time


def intro():
    step1 = """ \n
    .88b  d88.  .d8b.  d8b   db .d8888. d888888b  .d88b.  d8b   db
    88'YbdP`88 d8' `8b 888o  88 88'  YP   `88'   .8P  Y8. 888o  88
    88  88  88 88ooo88 88V8o 88 `8bo.      88    88    88 88V8o 88
    88  88  88 88~~~88 88 V8o88   `Y8b.    88    88    88 88 V8o88
    88  88  88 88   88 88  V888 db   8D   .88.   `8b  d8' 88  V888
    YP  YP  YP YP   YP VP   V8P `8888Y' Y888888P  `Y88P'  VP   V8P
"""
    step2 = step1 + """ \n \n
        .o88b. db      d88888b  .d8b.  d8b   db d88888b d8888b.
       d8P  Y8 88      88'     d8' `8b 888o  88 88'     88  `8D
       8P      88      88ooooo 88ooo88 88V8o 88 88ooooo 88oobY'
       8b      88      88~~~~~ 88~~~88 88 V8o88 88~~~~~ 88`8b
       Y8b  d8 88booo. 88.     88   88 88  V888 88.     88 `88.
        `Y88P' Y88888P Y88888P YP   YP VP   V8P Y88888P 88   YD
"""

    step3 = step2 + """ \n \n
                   db .d888b. .d888b. .d888b.
                  o88 88' `8D 88' `8D 88   8D
                   88 `V8o88' `V8o88' `VoooY'
                   88    d8'     d8'  .d~~~b.
                   88   d8'     d8'   88   8D
                   VP  d8'     d8'    `Y888P'
"""
    os.system('clear')
    print(step1)
    time.sleep(.5)
    os.system('clear')
    print(step2)
    time.sleep(.5)
    os.system('clear')
    print(step3)
    time.sleep(1)
    os.system('clear')

def main():
    intro()
    "Create a new game"
    game = Game.Game()
    "Display the mansion"
    mansion = game.get_current_mansion()
    "Create the worker"
    game.create_new_robot(mansion)
    robot = game.get_robot()
    robot.print_environment()
    "Let's get to work !"
    game.start_robot()

if __name__ == "__main__":
    main()
