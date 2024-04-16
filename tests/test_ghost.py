import pytest
from ghosts.Blinky import Blinky
from Player import Player
import pygame


@pytest.fixture
def blinky():
    player = Player(x=100, y=200, lives_count=3, direction=0, player_speed=2, maze=None)
    return Blinky(player)


@pytest.mark.parametrize("width, height, expected_turns", [
    (800, 600, [False, True, True, True]),
    (400, 500, [True, False, True, False]),
])
def test_can_move(blinky, width, height, expected_turns):
    blinky.can_move(width=width, height=height)
    assert blinky.turns == expected_turns


def test_update(blinky):
    blinky.update(powerup=True)
    assert blinky.image == blinky.powerup_img
    blinky.update(powerup=False)
    assert blinky.image == blinky.normal_img


def test_choose_target(blinky):
    blinky.powerup = True
    assert blinky.choose_target() is blinky.powerup_player
    blinky.powerup = False
    assert blinky.choose_target() is blinky.player

