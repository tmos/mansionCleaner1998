import random
import emoji
import time
import os
import constants
import Node

class Robot:
    """
        Heuristically Programmed Algorithmic computer n°9000.
        Also known as HAL 9000.
        Originally created for Discovery One ship, but finally used
        as a domestic hoover. Less risky.
    """
    score = 100
    cleaned_dust = 0
    stored_jewels = 0
    lost_jewels = 0
    cycles = 0

    current_move = 0
    available_moves = 10

    mansion = None
    position = {'x': -1, 'y': -1}
    current_cell = ''
    targets = []
    actions = []

    def __init__(self, mansion):
        """Hal's birthplace"""
        self.mansion = mansion
        self.mansion_dimensions = mansion.get_mansion_dimensions()
        self.position['x'] = random.randint(0, self.mansion_dimensions['width'] - 1)
        self.position['y'] = random.randint(0, self.mansion_dimensions['height'] - 1)

    def live(self):
        while True:
            self.mansion.populate()

            if self.current_move < self.available_moves:
                self.current_move += 1

            if len(self.actions) is 0 or self.current_move == self.available_moves:
                if self.look_for_new_targets():
                    self.think()
                self.current_move = 0

            self.act()

            # Utilities
            self.print_environment()
            self.cycles += 1
            time.sleep(0.25)

    def look_for_new_targets(self):
        """Capteur"""

        board = self.mansion.board
        new_targets = []

        self.modify_score(-2)

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
            goals = find_goals(robot)

            # Set of all A*'s best paths
            path_set = []

            for goal in goals:
                # Do A* calculation for each goal
                path_set.append(a_star(start, goal))

            best_path = []
            g_score = 0
            max_elements = 0
            for path in path_set:
                elements = path[0]
                move = path[1]
                # Intelligence is here
                if ((elements > max_elements) and (len(move) <= robot.available_moves)) \
                        or ((elements == max_elements) and (len(move) <= robot.available_moves) and (move[-1].g_score < g_score)):
                    best_path = move
                    max_elements = elements
                    g_score = move[-1].g_score

            return convert_path_to_move(best_path)

        def find_goals(robot):
            """Return every potential goals"""
            goals = []
            for target in robot.targets:
                goals.append(Node.Node(target[1], target[0], robot.mansion.board[target[1]][target[0]]))
            return goals

        def convert_path_to_move(path):
            """Convert a node path to a move path"""
            moves = []
            prev_x = path[0].x
            prev_y = path[0].y

            for node in path:
                if (node.x == prev_x + 1) and (node.y == prev_y):
                    prev_x = node.x
                    moves.append(constants.RIGHT)
                elif (node.x == prev_x - 1) and (node.y == prev_y):
                    prev_x = node.x
                    moves.append(constants.LEFT)
                elif (node.x == prev_x) and (node.y == prev_y + 1):
                    prev_y = node.y
                    moves.append(constants.DOWN)
                elif (node.x == prev_x) and (node.y == prev_y - 1):
                    prev_y = node.y
                    moves.append(constants.UP)
                elif (node.x != prev_x) and (node.y != prev_y):
                    return False
                if self.mansion.board[node.y][node.x] is constants.JEWEL:
                    moves.append(constants.TAKE)
                elif self.mansion.board[node.y][node.x] is constants.DUST:
                    moves.append(constants.CLEAN)
                elif self.mansion.board[node.y][node.x] is constants.BOTH:
                    moves.append(constants.TAKE)
                    moves.append(constants.CLEAN)

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
            number_of_elements = 0
            if current.weight == constants.BOTH_WEIGHT:
                number_of_elements = 2
            elif (current.weight == constants.JEWEL_WEIGHT) or (current.weight == constants.DUST_WEIGHT):
                number_of_elements = 1
            total_path = [current]
            while current.came_from:
                current = current.came_from
                total_path = [current] + total_path
                if current.weight == constants.BOTH_WEIGHT:
                    number_of_elements += 2
                elif (current.weight == constants.JEWEL_WEIGHT) or (current.weight == constants.DUST_WEIGHT):
                    number_of_elements += 1
            return [number_of_elements, total_path]

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
                neighbors.append(Node.Node(current_x-1, current_y, self.mansion.board[current_y][current_x-1]))
            if current_x < x_max:
                neighbors.append(Node.Node(current_x+1, current_y, self.mansion.board[current_y][current_x+1]))
            if current_y > y_min:
                neighbors.append(Node.Node(current_x, current_y-1, self.mansion.board[current_y-1][current_x]))
            if current_y < y_max:
                neighbors.append(Node.Node(current_x, current_y+1, self.mansion.board[current_y+1][current_x]))
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

        actions = find_move(self)
        if self.score//10 > 0:
            self.available_moves = self.score//10
        else :
            self.available_moves = 3

        self.actions = actions[:self.available_moves]

    def act(self):
        """Do what you need to do"""

        if self.actions:
            self.do_something(self.actions.pop(0))

    def do_something(self, action):
        """Déplacement"""

        got_something = False
        got_wrong = False
        did_something = None
        current_cell = self.get_current_cell()

        if action is constants.UP:
            if self.position['y'] > 0:
                self.position['y'] -= 1
                did_something = True

        elif action is constants.DOWN:
            if self.position['y'] < self.mansion_dimensions['height'] - 1:
                self.position['y'] += 1
                did_something = True

        elif action is constants.RIGHT:
            if self.position['x'] < self.mansion_dimensions['width'] - 1:
                self.position['x'] += 1
                did_something = True

        elif action is constants.LEFT:
            if self.position['x'] > 0:
                self.position['x'] -= 1
                did_something = True

        elif action is constants.CLEAN:
            if current_cell is constants.DUST:
                self.cleaned_dust += 1
                got_something = True
            elif current_cell is constants.JEWEL or current_cell is constants.BOTH:
                self.lost_jewels += 1
                got_wrong = True
            self.mansion.board[self.position['y']][self.position['x']] = constants.EMPTY
            did_something = True

        elif action is constants.TAKE:
            if current_cell is constants.JEWEL:
                self.stored_jewels += 1
                got_something = True
                self.mansion.board[self.position['y']][self.position['x']] = constants.EMPTY
            elif current_cell is constants.BOTH:
                self.stored_jewels += 1
                got_something = True
                self.mansion.board[self.position['y']][self.position['x']] = constants.DUST

            did_something = True

        if did_something:  # Energy
            self.modify_score(-1)
        if got_wrong:
            self.modify_score(-100)
        elif got_something:
            self.modify_score(+10)

    def get_current_cell(self):
        return self.mansion.board[self.position['y']][self.position['x']]

    def modify_score(self, value):
        if self.score + value < 0:
            self.score = 0
        else:
            self.score += value

    def print_environment(self):
        """Display the mansion in the terminal"""

        board = self.mansion.board

        os.system('clear')

        print(' ' + emoji.emojize(constants.DUST, use_aliases=True) + '  Dust : ' + str(self.cleaned_dust) + '\n')
        print(' ' + emoji.emojize(constants.JEWEL, use_aliases=True) + '  Jewels : ' + str(self.stored_jewels) + '\n')
        print(' ' + emoji.emojize(constants.JEWEL, use_aliases=True) + '  Lost jewels : ' + str(self.lost_jewels) + '\n')
        print(' ' + emoji.emojize(':arrows_clockwise:', use_aliases=True) + '  Cycles : ' + str(self.cycles) + '\n')
        print(' ' + emoji.emojize(':heavy_check_mark:', use_aliases=True) + '  Score : ' + str(self.score) + '\n')
        print('  Tours : ' + str(self.current_move) + '/' + str(self.available_moves))
        for i in range(len(board)):
            line_text = ''

            for j in range(len(board[i])):
                line_text += " "

                if i == self.position['y'] and j == self.position['x']:
                    line_text += ":sunglasses:"
                else:
                    line_text += board[i][j]

                line_text += " "

            print(emoji.emojize(line_text, use_aliases=True) + '\n')

        print("Upcoming  moves : \n")
        print(self.actions)
