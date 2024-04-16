import pytest
from ghosts.Blinky import Blinky
from Player import Player


@pytest.fixture
def blinky(mocker):
    def mock_image_load(_, path):
        return mocker.MagicMock()

    mocker.patch('pygame.transform.scale', side_effect=mock_image_load)
    player = Player(x=100, y=200, lives_count=3, direction=0, player_speed=2, maze=None)
    return Blinky(player)
