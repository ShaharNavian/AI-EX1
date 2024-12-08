from grid_robot_state import grid_robot_state


def base_heuristic(_grid_robot_state):
    # Calculate Manhattan distance between the robot and the lamp
    return (abs(_grid_robot_state.location[0] - _grid_robot_state.lamp_location[0]) +
            abs(_grid_robot_state.location[1] - _grid_robot_state.lamp_location[1]))


def advanced_heuristic(_grid_robot_state):
    # Unpack necessary info
    lamp_x, lamp_y = _grid_robot_state.lamp_location
    lamp_height_needed = _grid_robot_state.lamp_height
    current_lamp_height = _grid_robot_state.map[lamp_x][lamp_y]
    stairs_in_hand = _grid_robot_state.staircase_height

    # Base is Manhattan distance to the lamp
    dist_to_lamp = abs(_grid_robot_state.location[0] - lamp_x) + abs(_grid_robot_state.location[1] - lamp_y)

    # Calculate how many stairs we still need
    needed_stairs = lamp_height_needed - current_lamp_height

    if needed_stairs <= 0:
        # No extra stairs are needed
        return dist_to_lamp
    else:
        # Stairs are needed
        if stairs_in_hand >= needed_stairs:
            # We already hold enough stairs to achieve the goal height
            # Just need to place them: small constant to represent the place cost
            return dist_to_lamp + 1
        else:
            # Not enough stairs in hand, must fetch more
            shortfall = needed_stairs - stairs_in_hand
            # Add a big penalty to represent searching, picking up, and returning with extra stairs.
            # This is a heuristic guess:
            #   - Double the distance to roughly account for a detour trip (going to get stairs and back)
            #   - Add a penalty per missing stair unit to reflect picking and placing them.
            return dist_to_lamp + (2 * dist_to_lamp) + (shortfall * 2)
