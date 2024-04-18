import pytest
from bonuses.heart import Heart


@pytest.fixture
def mock_maze(mocker):
    # Mock maze object
    return mocker.MagicMock()


@pytest.fixture
def heart_instance(mock_maze):
    # Create an instance of Heart class with mock maze
    return Heart(0, 0, mock_maze)


def test_heart_draw(heart_instance, mocker):
    # Mock screen object
    mock_screen = mocker.Mock()

    # Call draw method
    heart_instance.draw(mock_screen)

    # Check if screen.blit method is called with correct arguments
    mock_screen.blit.assert_called_once_with(heart_instance.image, heart_instance.rect)




@pytest.mark.parametrize("initial_lives_count, expected_lives_count", [
    (0, 1),  # Test when initial lives count is 0
    (2, 3),  # Test when initial lives count is 2
    (-1, 0), # Test when initial lives count is negative
])
def test_hit(heart_instance, mock_maze, initial_lives_count, expected_lives_count):
    mock_maze.player.lives_count = initial_lives_count
    heart_instance.hit()
    assert mock_maze.player.lives_count == expected_lives_count
