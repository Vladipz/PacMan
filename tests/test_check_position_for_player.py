import pytest


# 0-RIGHT, 1-LEFT, 2-UP, 3-DOWN
@pytest.mark.parametrize(
    "center_x, center_y, direction, expected_turns",
    [
        (73, 74, 3, [False, False, True, False]),
        (39, 40, 1, [True, False, False, False]),
        (113, 104, 2, [False, False, False, False]),
    ],
)
def test_check_position(
    maze_with_huge_map, center_x, center_y, direction, expected_turns
):
    maze_with_huge_map.player.direction = direction
    turns = maze_with_huge_map.check_position(center_x, center_y)
    assert turns == expected_turns
