from typing import Tuple, List

import numpy as np


class Node(object):
    """ A node class for A* Pathfinding
    """

    def __init__(self, parent=None, position: Tuple[int, int] = None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def move(self, x: int, y: int) -> Tuple[int, int]:
        """get new position

        Arguments:
            x {int} -- x dim movement
            y {int} -- y dim movement

        Returns:
            Tuple[int, int] -- result positon for movement
        """

        position = self.position
        new_position = (position[0] + x, position[1] + y)
        return new_position

    def update_value(self, current_node, end_node):
        """ update g, h, f value depend on node

            Arguments:
                node {Node} -- current node
        """
        self.g = current_node.g + 1.
        self.h = (self.position[0] - end_node.position[0])**2 + \
            (self.position[1] - end_node.position[1])**2
        self.f = self.g + self.h

    def __eq__(self, other):
        return self.position == other.position


class Maze(object):

    def __init__(self, maze_array: List):
        self.maze_array = np.array(maze_array, dtype=np.int)

    def is_in_maze(self, position: Tuple[int, int]) -> bool:
        height, width = self.maze_array.shape

        if position[0] < 0 or position[1] < 0:
            return False
        elif position[0] < width and position[1] < height:
            return True
        else:
            return False

    def is_terrain(self, position: Tuple[int, int]) -> bool:
        maze_array = self.maze_array

        if maze_array[position[0], position[1]] == 0:
            return False
        else:
            return True
