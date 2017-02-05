import random
import emoji
import time
import os
import objects


UP = 'UP'
DOWN = 'DOWN'
LEFT = 'LEFT'
RIGHT = 'RIGHT'

class Robot:
    """
        Heuristically Programmed Algorithmic computer n°9000.
        Also known as HAL 9000.
        Originally created for Discovery One ship, but finally used
        as a domestic hoover. Less risky.
    """
    score = 0
    mansion = None
    position = {'x': 0, 'y': 0}
    current_cell = ''
    cleaned_dust = 0
    stored_jewels = 0
    cycles = 0
    energy = 0
    targets = []
    moves = []

    def __init__(self, mansion):
        """Hal's birthplace"""
        self.mansion = mansion
        self.mansion_dimensions = mansion.get_mansion_dimensions()
        self.position['x'] = random.randint(0, self.mansion_dimensions['width'] - 1)
        self.position['y'] = random.randint(0, self.mansion_dimensions['height'] - 1)

    def live(self):
        go = True
        while go:
            self.mansion.populate()
            self.current_cell = self.mansion.board[self.position['x']][self.position['y']]

            """BEGIN Temporary"""
            tmp = random.randint(0, 4)
            if tmp == 0:
                self.move(UP)
            elif tmp == 1:
                self.move(DOWN)
            elif tmp == 2:
                self.move(LEFT)
            elif tmp == 3 :
                self.move(RIGHT)
            else:
                """freeze !"""
            self.clean()
            """END Temporary"""

            """
            if self.look_for_new_targets() is not None:
                self.think()
                self.act()
            """

            self.print_environment()
            self.cycles += 1
            time.sleep(.075)
            """go = None"""

    def look_for_new_targets(self):
        """Capteur"""

        board = self.mansion.board
        targets = []

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] is not objects.EMPTY:
                    targets.append([i, j])

        if self.targets != targets:
            self.targets = targets
            return targets
        else:
            return None

    def think(self):
        """What are the most efficient moves ?"""
        self.moves = []
        """
        Algo de chemin le plus optimisé
        """
        self.moves.append(DOWN)

    def act(self):
        """Do what you need to do"""
        self.move(self.moves.pop())
        self.clean()

    def clean(self):
        """Effecteur. Another one bytes the dust !"""

        if self.current_cell is not objects.EMPTY:
            if self.current_cell is objects.DUST:
                self.cleaned_dust += 1

            if self.current_cell is objects.JEWEL:
                self.stored_jewels += 1

            self.mansion.board[self.position['x']][self.position['y']] = '·'

    def move(self, direction):
        """Déplacement"""

        has_moved = None

        if direction is UP:
            if self.position['x'] > 0:
                self.position['x'] -= 1
                has_moved = True

        elif direction is DOWN:
            if self.position['x'] < self.mansion_dimensions['width'] - 1:
                self.position['x'] += 1
                has_moved = True

        elif direction is RIGHT:
            if self.position['y'] < self.mansion_dimensions['height'] - 1:
                self.position['y'] += 1
                has_moved = True

        elif direction is LEFT:
            if self.position['y'] > 0:
                self.position['y'] -= 1
                has_moved = True
        else:
            "wtf"

        if has_moved:
            self.energy += 1

    def print_environment(self):
        """Display the mansion in the terminal"""

        board = self.mansion.board

        os.system('clear')

        print('>> Dust : ' + str(self.cleaned_dust) + '\n')
        print('>> Jewels : ' + str(self.stored_jewels) + '\n')
        print('>> Cycles : ' + str(self.cycles) + '\n')
        print('>> Energy : ' + str(self.energy) + '\n')

        for i in range(len(board)):
            line_text = ''

            for j in range(len(board[i])):
                line_text += " "

                if i == self.position['x'] and j == self.position['y']:
                    line_text += ":snail:"
                else:
                    line_text += board[i][j]

                line_text += " "

            print(emoji.emojize(line_text, use_aliases=True) + '\n')
