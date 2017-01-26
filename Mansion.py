import random
import emoji


class Mansion:
    """
    A big mansion, with a penthouse, a pool, a big garage.
    Note that the place may be dusty, and some objects can be found on the floor.
    But don't worry. Robot.py is here to handle that.
    """
    EMPTY = '·'
    DUST = ':hankey:'
    JEWEL = ':ring:'
    board = []

    def __init__(self, w=random.randint(8, 16), h=random.randint(8, 16)):
        """Create a new mansion"""

        self.w = w
        self.h = h
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

    def get_mansion_dimensions(self):
        return {'width': len(self.board), 'height': len(self.board[0])}
