# setting files for astar

POSITIONS = [(0, -1), (0, 1), (-1, 0), (1, 0),
             (-1, -1), (-1, 1), (1, -1), (1, 1)]

# Basic setting
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 600
FPS = 5
MAZE_TOP = 50
MAZE_LEFT = 50
CELL_HEIGHT = 50
CELL_WIDTH = 50

# Color setting
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WALL = (102, 51, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (0, 255, 0)
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
