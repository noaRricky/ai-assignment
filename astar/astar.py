from typing import Tuple, List

import numpy as np

POSITIONS = [(0, -1), (0, 1), (-1, 0), (1, 0),
             (-1, -1), (-1, 1), (1, -1), (1, 1)]


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

    def __eq__(self, other: Tuple):
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


def astar(maze: Maze, start: Tuple, end: Tuple) -> List[Tuple]:
    """Applying A* alogrithm

    Arguments:
        maze {List} -- maze
        start {Tuple} -- start point
        end {Tuple} -- end point

    Returns:
        List[Tuple] -- a path from start point to end point save in a list of tuple
    """

    # Initialize the start and end node
    start_node = Node(parent=None, position=start)
    start_node.g = start_node.h = start_node.f = float(0)
    end_node = Node(parent=None, position=end)
    end_node.g = end_node.h = end_node.f = float(0)

    # Initialize the list
    open_list = []
    close_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:
        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current node in open list, and add to close list
        open_list.pop(current_index)
        close_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]  # Reverse the path

        # Else generate the children
        children = []
        for new_position in POSITIONS:
            # Get new node position
            node_position = current_node.move(new_position[0], new_position[1])

            # Make sure within range
            if not maze.is_in_maze(node_position):
                continue

            if maze.is_terrain(node_position):
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:
            # Child is on the close list
            for close_child in close_list:
                if child == close_child:
                    continue

            # update the f, g, and h valuse
            child.update_value(current_node, end_node)
            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)


def main():
    """The main function"""
    maze_array = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    start = (0, 0)
    end = (7, 6)
    maze = Maze(maze_array)

    path = astar(maze, start, end)
    print(path)


if __name__ == "__main__":
    main()
