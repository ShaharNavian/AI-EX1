import time
from heuristics import *
from search import *

if __name__ == '__main__':
    map = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, -1, 0, 0, 1, 0, 0],
        [0, -1, 1, 0, 2, 0, -1, 0],
        [0, 0, 2, 0, -1, 1, 0, 0],
        [0, 0, 2, 1, 0, 3, 0, 0],
        [-1, 1, 0, -1, 0, -1, 0, 0],
        [-1, 0, -1, 0, 0, 1, 0, -1],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]
    robot_start_location = (7, 0)
    lamp_h = 4
    lamp_location = (0, 4)

    start_state = grid_robot_state(map=map, robot_location=robot_start_location, lamp_height=lamp_h,
                                   lamp_location=lamp_location)
    start_time = time.time()
    search_result = search(start_state, advanced_heuristic)
    end_time = time.time() - start_time
    # runtime
    print(end_time)
    # for node in search_result:
    #     print(node.state.get_state_str())
    #     print(node.state.map)
    # solution cost
    print(search_result[-1].g)
