import pytest
from maze import Maze
from settings import *
import pygame


@pytest.fixture
def mock_maze(mocker):
    # Mock maze object
    return mocker.MagicMock()


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
    maze_instance.level = [[0, 0, 0], [1, 0, 1], [0, 0, 0]]
    # random.seed(42)  # Set seed for reproducibility
    assert maze_instance.find_coordinates_for_health() == (1, 0) or (1, 2)


# def mock_check_point_on_board_1():
#     return 0  # For example, always return 0 for testing purposes
#
#
# def mock_check_point_on_board_2():
#     return 5  # For example, always return 5 for testing purposes


@pytest.mark.parametrize("mocked_method", [lambda: 0, lambda: 5])
def test_check_win_with_mocked_method(maze_instance, monkeypatch, mocked_method):
    # Use monkeypatch to substitute the method
    monkeypatch.setattr(maze_instance, "check_point_on_board", mocked_method)

    # Now, check_win should return True or False based on the mocked_method
    assert maze_instance.check_win() == (True if mocked_method() == 0 else False)


def test_find_coordinates_for_health_default_value(mocker):
    # Arrange
    maze_instance = Maze(color="blue", width=3, height=3, screen=None)
    # Mocking check_point_on_board to always return 1
    mocker.patch.object(maze_instance, "check_point_on_board", return_value=1)

    # Act
    coordinates = maze_instance.find_coordinates_for_health()

    # Assert
    assert coordinates == (
        2,
        2,
    )


def test_check_collisions_with_no_collision(maze_instance):
    # Arrange
    score = 0
    center_x = 100
    center_y = 100
    power = False
    power_count = 0
    eaten_ghosts = [False, False, False, False]

    # Act
    score, power, power_count, eaten_ghosts = maze_instance.check_collisions(
        score, center_x, center_y, power, power_count, eaten_ghosts
    )

    # Assert
    assert score == 0
    assert power == False
    assert power_count == 0
    assert eaten_ghosts == [False, False, False, False]


def test_check_collisions_with_point_collision(maze_instance):
    # Arrange
    score = 0
    center_x = 60
    center_y = 60
    power = False
    power_count = 0
    eaten_ghosts = [False, False, False, False]

    # Act
    score, power, power_count, eaten_ghosts = maze_instance.check_collisions(
        score, center_x, center_y, power, power_count, eaten_ghosts
    )

    # Assert
    assert score == 10  # Assuming score increases by 10 when a point is collected
    assert power == False
    assert power_count == 0
    assert eaten_ghosts == [
        False,
        False,
        False,
        False,
    ]  # No change in eaten_ghosts list


def test_check_collisions_with_big_dot(maze_instance, mocker):
    # Arrange
    score = 0
    center_x = 60  # Center X coordinate of the player over a big dot
    center_y = 122  # Center Y coordinate of the player over a big dot
    power = False
    power_count = 0
    eaten_ghosts = [False, False, False, False]
    num1 = (maze_instance.height - 50) // 32
    num2 = maze_instance.width // 30
    print(center_y // num1, center_x // num2)
    # Mocking pygame.time.set_timer method
    mocker.patch.object(pygame.time, "set_timer")

    # Act
    score, power, power_count, eaten_ghosts = maze_instance.check_collisions(
        score, center_x, center_y, power, power_count, eaten_ghosts
    )

    # Assert
    assert score == 50  # Score should increase by 50 after colliding with a big dot
    assert power is True  # Power should be activated after colliding with a big dot
        # Additional assertions can be added to test other aspects of the method
