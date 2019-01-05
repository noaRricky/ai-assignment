from typing import Tuple, List
import pygame
import numpy as np

from astar import Maze, astar

# Basic setting
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 600
FPS = 30
MAZE_TOP = 50
MAZE_LEFT = 50
CELL_HEIGHT = 50
CELL_WIDTH = 50

# Color setting
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WALL = (102, 51, 0)
ORANGE = (0, 128, 255)

# Maze setting
MAZE_ARRAY = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
START_POINT = (0, 0)
END_POINT = (7, 6)

# init pygame env
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()


def draw_cell(row: int, col: int, cell_color: Tuple[int, int, int]) -> None:
    cell_top = MAZE_TOP + row * CELL_HEIGHT
    cell_left = MAZE_LEFT + col * CELL_WIDTH
    pygame.draw.rect(screen, cell_color, pygame.Rect(
        cell_left, cell_top, CELL_WIDTH, CELL_HEIGHT))


def draw_maze(maze: Maze, start: Tuple[int, int], end: Tuple[int, int]) -> None:
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


def draw_path(path: List[Tuple[int, int]]) -> None:
    """ draw path

    Arguments:
        path {List[Tuple[int, int]]} -- draw path
    """
    for row, col in path:
        draw_cell(row, col, ORANGE)
    return


def main():

    # Initialize maze parameter
    maze = Maze(MAZE_ARRAY)

    path = None
    find_path = False
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                find_path = True

        screen.fill(BLACK)

        draw_maze(maze, START_POINT, END_POINT)

        if find_path:
            path = astar(maze, START_POINT, END_POINT)
            # draw_path(path)
            find_path = False

        if path is not None:
            draw_path(path)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
