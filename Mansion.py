import random


class Mansion:
    EMPTY = '·'
    DUST = 'd'
    JEWEL = 'j'
    board = []

    def __init__(self, w=random.randint(8, 16), h=random.randint(8, 16)):
        """Create a new mansion"""
        self.board = [[self.EMPTY for x in range(w)] for y in range(h)]
        self.populate()

    def populate(self):
        """Populate the mansion with jewel and dust"""
        lines = range(len(self.board))

        for line in lines:
            cases = range(len(self.board[line]))

            for case in cases:
                if self.board[line][case] is self.EMPTY:
                    tmp_rand = random.randint(0, 19)
                    "18/20 chances to be empty"

                    if tmp_rand == 0:
                        self.board[line][case] = self.DUST
                    elif tmp_rand == 1:
                        self.board[line][case] = self.JEWEL
                    else:
                        self.board[line][case] = self.EMPTY

    def print_mansion(self):
        """Display the mansion in the terminal"""
        for i in range(len(self.board)):
            line_text = ''

            for j in range(len(self.board[i])):
                line_text += " " + self.board[i][j]

            print(line_text + '\n')
