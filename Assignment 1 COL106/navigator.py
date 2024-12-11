from maze import *
from exception import *
from stack import *
class PacMan:
    def __init__(self, grid : Maze) -> None:
        ## DO NOT MODIFY THIS FUNCTION
        self.navigator_maze = grid.grid_representation
    def find_path(self, start : tuple[int, int], end : tuple[int, int]) -> list[tuple[int, int]]:
        # IMPLEMENT FUNCTION HERE
        raise PathNotFoundException
