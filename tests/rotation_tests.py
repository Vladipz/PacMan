import pytest
import pygame
import pytest
from Player import Player
from maze import Maze
import maze


@pytest.fixture
def player():
    color = (255, 255, 255)  # Приклад значення кольору
    width = 800  # Приклад значення ширини
    height = 600  # Приклад значення висоти
    screen = pygame.display.set_mode((width, height))  # Створення екрану pygame

    maze_grid = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    maze = Maze(color, width, height, screen)
    maze.level = maze_grid
    # Створюємо екземпляр класу Player
    return Player(0, 0, 3, 0, 0, maze)


maze_new = Maze((255, 255, 255), 800, 600, screen=pygame.display.set_mode((800, 600)))
pla = Player(0, 0, 3, 0, 0, maze_new)


@pytest.mark.parametrize("direction, counter, expected_image", [
    (0, 0, pla.player_images[0]),
    (1, 1, pla.player_images[1]),
    (2, 2, pla.player_images[2]),
    (3, 3, pla.player_images[3])])
def test_draw_player(player, direction, counter, expected_image):
    player.direction = direction
    image = player.maze.draw_player_for_tests(counter)
    assert image == expected_image
