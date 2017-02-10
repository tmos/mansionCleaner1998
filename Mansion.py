import random
import emoji
import constants


class Mansion:
    """
    A big mansion, with a penthouse, a pool, a big garage.
    Note that the place may be dusty, and some objects can be found on the floor.
    But don't worry. Robot.py is here to handle that.
    """

    board = []

    def __init__(self, w=5, h=5):
        """Create a new mansion"""

        self.w = w
        self.h = h
        self.board = [[constants.EMPTY for x in range(w)] for y in range(h)]

    def populate(self):
        """Populate the mansion with jewel and dust"""
        lines = range(len(self.board))
        for line in lines:
            cases = range(len(self.board[line]))

            for case in cases:
                if self.board[line][case] is constants.EMPTY:
                    tmp_rand = random.randint(0, 1000)
                    "18/20 chances to be empty"

                    if tmp_rand == 0:
                        self.board[line][case] = constants.DUST
                    elif tmp_rand == 1:
                        self.board[line][case] = constants.JEWEL
                    else:
                        self.board[line][case] = constants.EMPTY

    def get_mansion_dimensions(self):
        return {'width': len(self.board), 'height': len(self.board[0])}
