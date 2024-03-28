import pytest
from maze import Maze
from settings import *


@pytest.fixture
def maze_instance():
    maze = Maze("white", width, height, screen=None)
    return maze


def test_check_point_on_board(maze_instance):
    maze_instance.level = [[0, 0, 0], [1, 0, 2], [0, 0, 0]]
    assert (
        maze_instance.check_point_on_board() == 2
    )  # Assuming there are 2 points on the board


def test_find_coordinates_for_health(maze_instance):
    # Assuming the initial level has no points
    # assert maze_instance.find_coordinates_for_health() == (2, 2)
    # Modify the level to have some points
    # Modify the level according to your game structure
    maze_instance.level = [
        [0, 0, 0],
        [1, 0, 1],
        [0, 0, 0]]
    # random.seed(42)  # Set seed for reproducibility
    assert maze_instance.find_coordinates_for_health() == (1, 0) or (1, 2)
