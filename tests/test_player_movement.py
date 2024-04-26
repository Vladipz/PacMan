import pytest


@pytest.mark.parametrize(
    "direction, turns_allowed, expected_x, expected_y",
    [
        (0, [True, False, False, False], 6, 4),  # Test moving right
        (1, [False, True, False, False], 2, 4),  # Test moving left
        (2, [False, False, True, False], 4, 2),  # Test moving down
        (3, [False, False, False, True], 4, 6),  # Test moving up
    ],
)
def test_player_move(
    maze_with_player, direction, turns_allowed, expected_x, expected_y
):
    maze_with_player.player.direction = direction
    maze_with_player.move_player(turns_allowed)
    assert expected_x == maze_with_player.player.x
    assert expected_y == maze_with_player.player.y
