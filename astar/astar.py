from typing import Tuple, List

import numpy as np
import pygame

from settings import *
from items import Maze, Node


# init pygame env
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()


def draw_cell(row: int, col: int, cell_color: Tuple[int, int, int]) -> None:
    """ draw cell

    Arguments:
        row {int} -- row in maze
        col {int} -- column in maze
        cell_color {Tuple[int, int, int]} -- the rgb code for cell color
    """

    cell_top = MAZE_TOP + row * CELL_HEIGHT
    cell_left = MAZE_LEFT + col * CELL_WIDTH
    pygame.draw.rect(screen, cell_color, pygame.Rect(
        cell_left, cell_top, CELL_WIDTH, CELL_HEIGHT))


def draw_maze(maze: Maze,
              start: Tuple[int, int],
              end: Tuple[int, int]) -> None:
    """ draw maze

    Arguments:
        maze {Maze} -- maze object
        start {Tuple[int, int]} -- start point
        end {Tuple[int, int]} -- end point
    """
    maze_array = maze.maze_array
    maze_height, maze_width = maze_array.shape

    # draw maze
    for row in range(maze_height):
        for col in range(maze_width):
            # set cell color
            if maze_array[row, col] == 0:
                cell_color = WHITE
            else:
                cell_color = WALL
            draw_cell(row, col, cell_color)

    # draw start and end point
    draw_cell(start[0], start[1], BLUE)
    draw_cell(end[0], end[1], RED)


def draw_path(path: List[Tuple[int, int]],
              cell_color: Tuple[int, int],) -> None:
    """ draw path

    Arguments:
        path {List[Tuple[int, int]]} -- draw path
    """
    for row, col in path:
        draw_cell(row, col, cell_color)
    return


def draw_node_list(node_list: List[Node], cell_color: Tuple[int, int]) -> None:
    for node in node_list:
        draw_cell(node.position[0], node.position[1], cell_color)


def astar(maze: Maze, start: Tuple, end: Tuple) -> List[Tuple]:
    """Applying A* alogrithm

    Arguments:
        maze {List} -- maze
        start {Tuple} -- start point
        end {Tuple} -- end point

    Returns:
        List[Tuple] -- a path from start point to
        end point save in a list of tuple
    """

    # Initialize the start and end node
    start_node = Node(parent=None, position=start)
    start_node.g = start_node.h = start_node.f = float(0)
    end_node = Node(parent=None, position=end)
    end_node.g = end_node.h = end_node.f = float(0)

    # Initialize the list
    open_list = []
    close_list = []
    path = []

    # Add the start node
    open_list.append(start_node)

    yield open_list, close_list

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
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            yield path[::-1]  # Reverse the path
            break

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

        yield open_list, close_list


def main():
    """main function"""

    # Initialize maze parameter
    maze = Maze(MAZE_ARRAY)

    path = None
    find_path = True
    running = True

    alg = astar(maze, START_POINT, END_POINT)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                find_path = False
                path = None

        screen.fill(BLACK)

        draw_maze(maze, START_POINT, END_POINT)

        if not find_path:
            try:
                path_list = alg.__next__()
            except StopIteration:
                find_path = True
            # draw_path(path)
            if len(path_list) == 2:
                draw_node_list(path_list[0], RED)
                draw_node_list(path_list[1], YELLOW)
            else:
                # print(path)
                path = path_list
                # find_path = True

        if path is not None:
            draw_path(path, ORANGE)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
