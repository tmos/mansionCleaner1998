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

    def populate(self, max_chances=50):
        """Populate the mansion with jewel and dust"""
        lines = range(len(self.board))
        for line in lines:
            cases = range(len(self.board[line]))

            for case in cases:
                tmp_rand = random.randint(0, max_chances)

                if tmp_rand == 0:
                    if self.board[line][case] is constants.JEWEL:
                        self.board[line][case] = constants.BOTH
                    elif self.board[line][case] is constants.EMPTY:
                        self.board[line][case] = constants.DUST

                elif tmp_rand == 1:
                    if self.board[line][case] is constants.DUST:
                        self.board[line][case] = constants.BOTH
                    elif self.board[line][case] is constants.EMPTY:
                        self.board[line][case] = constants.JEWEL


    def get_mansion_dimensions(self):
        return {'width': len(self.board), 'height': len(self.board[0])}
