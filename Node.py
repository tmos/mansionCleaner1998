import constants


class Node:
    """The node the robot uses to represent a case"""

    # The x position
    x = None

    # The y position
    y = None

    # The previous node, chosen by efficiency
    came_from = None

    # The weight value of this node
    weight = 0

    # The cost of getting from the start node to that node
    g_score = 0

    # The total cost of getting from the start node to the goal, using this node
    f_score = constants.INFINITY

    def __init__(self, x, y, cell):
        """Create a new node"""

        self.x = x
        self.y = y

        # Weight calculation
        if cell is not None:
            if cell is constants.EMPTY:
                self.weight = constants.EMPTY_WEIGHT
            if cell is constants.DUST:
                self.weight = constants.DUST_WEIGHT
            if cell is constants.JEWEL:
                self.weight = constants.JEWEL_WEIGHT
            # TODO add both weight
        self.g_score = self.weight
        # TODO calcul de fscore ?

    def equals(self, node):
        return (self.x == node.x) and (self.y == node.y)

    def belongs_to(self, nodes):
        for node in nodes:
            if (self.x == node.x) and (self.y == node.y):
                return True
        return False
