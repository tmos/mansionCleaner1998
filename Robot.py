import random
import emoji
import time
import os
import constants
import Node

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
    cleaned_dust = 0
    stored_jewels = 0
    cycles = 0
    spent_energy = 1
    mansion = None
    position = {'x': -1, 'y': -1}
    current_cell = ''
    targets = []
    path = []

    def __init__(self, mansion):
        """Hal's birthplace"""
        self.mansion = mansion
        self.mansion_dimensions = mansion.get_mansion_dimensions()
        self.position['x'] = random.randint(0, self.mansion_dimensions['width'] - 1)
        self.position['y'] = random.randint(0, self.mansion_dimensions['height'] - 1)

    def live(self):
        go = True
        while go:
            self.mansion.populate(50)

            if self.look_for_new_targets() is not None:
                self.think()

            self.act()

            self.print_environment()
            self.cycles += 1
            time.sleep(.025)

    def look_for_new_targets(self):
        """Capteur"""

        board = self.mansion.board
        new_targets = []

        self.spent_energy += 1

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] is not constants.EMPTY:
                    new_targets.append([i, j])

        if self.targets != new_targets:
            self.targets = new_targets
            return new_targets
        else:
            return None

    def think(self):
        """What are the most efficient moves ?"""

        def find_move(robot):
            start = Node.Node(robot.position['x'], robot.position['y'], robot.get_current_cell())
            goals = find_goals()

            # Set of all A*'s best paths
            path_set = []

            for goal in goals:
                # Do A* calculation for each goal
                path_set.append(a_star(start, goal))

            best_path = []
            best_g_score = constants.INFINITY
            for path in path_set:
                # Save the best path : the one with the lowest goal's g_score
                # TODO modifier les constantes pour que le g_score d'un chemin long
                # avec que des objets tout le long soit meilleur qu'un chemin beaucoup
                # plus court mais avec qu'un objet
                if path[-1].g_score < best_g_score:
                    best_path = path
                    best_g_score = path[-1].g_score

            # TODO savoir sous quel format on retourne le chemin,
            # l'utilisation de la classe Node n'est probablement pas pertinente en dehors de cette fonction
            robot.path = convert_path_to_move(best_path, best_g_score)
            # self.path.append({'moves': [], 'score': 1})"

        def find_goals():
            """Return every potential goals"""
            # TODO
            goals = []
            mansion_dimensions = self.mansion.get_mansion_dimensions()
            x_size = mansion_dimensions['width']
            y_size = mansion_dimensions['height']
            for x in range(0, x_size):
                for y in range(0, y_size):
                    if (self.mansion.board[x][y] is constants.DUST) or (self.mansion.board[x][y] is constants.JEWEL):
                        # TODO ajouter quand y a les deux
                        goals.append(Node.Node(x, y, self.mansion.board[x][y]))
            return goals

        def convert_path_to_move(path, score):
            """Convert a node path to a move path"""
            moves = []
            prev_x = path[0].x
            prev_y = path[0].y

            # TODO verifier les moves
            for node in path:
                if (node.x == prev_x + 1) and (node.y == prev_y):
                    prev_x = node.x
                    moves.append(RIGHT)
                elif (node.x == prev_x - 1) and (node.y == prev_y):
                    prev_x = node.x
                    moves.append(LEFT)
                elif (node.x == prev_x) and (node.y == prev_y + 1):
                    prev_y = node.y
                    moves.append(DOWN)
                elif (node.x == prev_x) and (node.y == prev_y - 1):
                    prev_y = node.y
                    moves.append(UP)
                elif (node.x != prev_x) and (node.y != prev_y):
                    return False
                if self.mansion.board[node.x][node.y] is constants.JEWEL:
                    moves.append(TAKE)
                elif self.mansion.board[node.x][node.y] is constants.DUST:
                    moves.append(CLEAN)

            return moves

        def a_star(start, goal):
            """A* algorithm"""

            # Start node f_score
            start.f_score = heuristic_cost_estimate(start, goal)

            # The set of node already evaluated
            closed_set = []

            # The set of currently discovered nodes that are not evaluated yet
            open_set = [start]

            # While open_set is not empty
            while open_set:
                # Chose as current the node in open_set having the lowest f_score value
                current = best_f_node(open_set)

                if current.equals(goal):
                    return reconstruct_path(current)

                open_set.remove(current)
                closed_set.append(current)

                # Find the neighbor nodes of current
                neighbor_set = neighbors_of(current)

                for neighbor in neighbor_set:
                    if neighbor.belongs_to(closed_set):  # if neighbor in closed_set:
                        # Ignore the neighbor which is already evaluated
                        continue

                    # Distance from start to the neighbor
                    tentative_g_score = current.g_score + neighbor.weight
                    # tentative_g_score = current.g_score + dist_between(current, neighbor)

                    if not neighbor.belongs_to(open_set):  # if neighbor not in open_set:
                        # Hurray! We discovered a new node
                        open_set.append(neighbor)
                    elif tentative_g_score >= neighbor.g_score:
                        # This is not a better path
                        continue

                    # This path is the best!
                    neighbor.came_from = current
                    neighbor.g_score = tentative_g_score
                    neighbor.f_score = neighbor.g_score + heuristic_cost_estimate(neighbor, goal)

            # Failure
            return False

        def reconstruct_path(current):
            """Return the path from the start node to the current node"""
            total_path = [current]
            while current.came_from:
                current = current.came_from
                total_path = [current] + total_path
            return total_path

        def neighbors_of(current):
            """Return the list of neighbor nodes of the current node"""
            neighbors = []
            mansion_dimensions = self.mansion.get_mansion_dimensions()
            current_x = current.x
            current_y = current.y
            x_min = 0
            y_min = 0
            x_max = mansion_dimensions['width']-1
            y_max = mansion_dimensions['height']-1
            if current_x > x_min:
                neighbors.append(Node.Node(current_x-1, current_y, self.mansion.board[current_x-1][current_y]))
            if current_x < x_max:
                neighbors.append(Node.Node(current_x+1, current_y, self.mansion.board[current_x+1][current_y]))
            if current_y > y_min:
                neighbors.append(Node.Node(current_x, current_y-1, self.mansion.board[current_x][current_y-1]))
            if current_y < y_max:
                neighbors.append(Node.Node(current_x, current_y+1, self.mansion.board[current_x][current_y+1]))
            return neighbors

        def best_f_node(node_set):
            best_node = node_set[0]

            for node in node_set:
                if node.f_score < best_node.f_score:
                    best_node = node

            return best_node

        def dist_between(current, node):
            return abs(current.x - node.x) + abs(current.y - node.y)

        def heuristic_cost_estimate(current, node):
            return dist_between(current, node) * constants.EMPTY_WEIGHT

        find_move(self)

    def act(self):
        """Do what you need to do"""

        if self.path:
            self.move(self.path.pop(0))
            self.clean()

    def clean(self):
        """Effecteur. Another one bytes the dust !"""
        # TODO : score is not increasing
        current_cell = self.get_current_cell()

        if current_cell is not constants.EMPTY:
            if current_cell is constants.DUST:
                self.cleaned_dust += 1
            if current_cell is constants.JEWEL:
                self.stored_jewels += 1

            self.score += 1
            self.mansion.board[self.position['x']][self.position['y']] = constants.EMPTY

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
            self.spent_energy += 1

    def get_ratio(self):
        return ((self.cycles / (self.spent_energy + (self.cleaned_dust + self.stored_jewels) * 2)) * 2) - 1

    def get_current_cell(self):
        return self.mansion.board[self.position['x']][self.position['y']]

    def print_environment(self):
        """Display the mansion in the terminal"""

        board = self.mansion.board

        os.system('clear')

        print(' ' + emoji.emojize(constants.DUST, use_aliases=True) + '  Dust : ' + str(self.cleaned_dust) + '\n')
        print(' ' + emoji.emojize(constants.JEWEL, use_aliases=True) + '  Jewels : ' + str(self.stored_jewels) + '\n')
        print(' ' + emoji.emojize(':arrows_clockwise:', use_aliases=True) + '  Cycles : ' + str(self.cycles) + '\n')
        print(' ' + emoji.emojize(':battery:', use_aliases=True) + '  Energy : ' + str(self.spent_energy) + '\n')
        print(' ' + emoji.emojize(':heavy_check_mark:', use_aliases=True) + '  Score : ' + str(self.get_ratio()) + '\n')

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

        print("path : \n")
        print(self.path)
