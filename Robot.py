import random
import emoji
import time


class Robot:
    """

    """
    score = 0
    mansion = None
    positions = {'x': 0, 'y': 0}

    def __init__(self, mansion):
        """Hal's birthplace"""
        self.mansion = mansion
        self.mansion_dimensions = mansion.get_mansion_dimensions()
        self.positions['x'] = random.randint(0, self.mansion_dimensions['width']-1)
        self.positions['y'] = random.randint(0, self.mansion_dimensions['height']-1)

    def live(self):
        while 1:
            time.sleep(1)

    def look(self):
        """Capteur"""

    def clean(self):
        """Effecteur. Another one bytes the dust !"""

    def move(self, direction):
        """Déplacement"""
        UP = 'UP'
        DOWN = 'DOWN'
        LEFT = 'LEFT'
        RIGHT = 'RIGHT'

        if direction is UP:
            if self.positions['x'] != 0:
                self.positions['x'] -= 1

        elif direction is DOWN:
            if self.positions['y'] != self.mansion_dimensions['y']:
                self.positions['y'] += 1

        elif direction is RIGHT:
            if self.positions['x'] != self.mansion_dimensions['x']:
                self.positions['x'] += 1

        elif direction is LEFT:
            if self.positions['y'] != 0:
                self.positions['y'] -= 1
        else:
            "wtf"

    def print_environment(self):
        """Display the mansion in the terminal"""
        board = self.mansion.board

        for i in range(len(board)):
            line_text = ''

            for j in range(len(board[i])):
                line_text += " "

                if i == self.positions['x'] and j == self.positions['y']:
                    line_text += ":snail:"
                else:
                    line_text += board[i][j]

                line_text += " "

            print(emoji.emojize(line_text, use_aliases=True) + '\n')
