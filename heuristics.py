from grid_robot_state import grid_robot_state

def base_heuristic(_grid_robot_state):
    # Calculate Manhattan distance between the robot and the lamp
    return (abs(_grid_robot_state.location[0] - _grid_robot_state.lamp_location[0]) +
            abs(_grid_robot_state.location[1] - _grid_robot_state.lamp_location[1]))

def advanced_heuristic(_grid_robot_state):
    # idea: Manhattan is goated idgaf about your opinion
    manhattan = base_heuristic(_grid_robot_state)
    height_difference = max(0, _grid_robot_state.lamp_height -
                            _grid_robot_state.map[_grid_robot_state.lamp_location[0]][_grid_robot_state.lamp_location[1]]
                            + _grid_robot_state.staircase_height)
    return pow(manhattan,2) + height_difference * 0.5 + 429  # Nuh uh, my heuristic, my RULES!!!
