import pytest

def test_check_collisions_condition_2(maze_with_huge_map):
    # Create an instance of YourClassName or mock it if needed
    # Initialize the necessary variables
    score = 0
    center_x = 64
    center_y = 32
    power = False
    power_count = 0
    eaten_ghosts = [False, False, False, False]

    # Call the specific part of the method
    # Assuming 'YourClassName' is instantiated as 'instance'
    result = maze_with_huge_map.check_collisions(score, center_x, center_y, power, power_count, eaten_ghosts)

    # Assert the changes made in this condition
    expected_result = (50, True, 0, [False, False, False, False])
    assert result[0] == expected_result[0]  # Score increased by 50
    assert result[1] == expected_result[1]  # Power set to True
    assert result[2] == expected_result[2]  # Power count reset to 0
    assert result[3] == expected_result[3]  # eaten_ghosts reset to [False, False, False, False]
