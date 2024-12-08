import time
from heuristics import advanced_heuristic, base_heuristic
from search import *
from grid_robot_state import grid_robot_state

if __name__ == '__main__':
    # Test 1: Mostly open 15x15 with a few stairs and a simple obstacle pattern
    map_test_1 = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, -1, -1, -1, 0, 0, 0, 0, -1, -1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    robot_start_location_1 = (0, 0)
    lamp_h_1 = 3
    lamp_location_1 = (10, 14)  # bottom-right corner region has a stair height 3 requirement

    start_state_1 = grid_robot_state(map=map_test_1, robot_location=robot_start_location_1, lamp_height=lamp_h_1,
                                     lamp_location=lamp_location_1)
    start_time = time.time()
    search_result_1 = search(start_state_1, advanced_heuristic)
    end_time = time.time() - start_time
    print("Test 1 runtime:", end_time)
    if search_result_1 is not None:
        print("Test 1 solution cost:", search_result_1[-1].g)
        print_path(search_result_1)
    else:
        print("Test 1: No path found")
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
    start_state_2 = grid_robot_state(map=map, robot_location=robot_start_location, lamp_height=lamp_h,
                                     lamp_location=lamp_location)
    start_time = time.time()
    search_result_1 = search(start_state_2, base_heuristic)
    end_time = time.time() - start_time
    print("Test 2 runtime:", end_time)
    if search_result_1 is not None:
        print("Test 2 solution cost:", search_result_1[-1].g)
        print_path(search_result_1)
    else:
        print("Test 2: No path found")
    map = [
        [0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, -1, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, -1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, -1, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 3]
    ]
    robot_start_location = (7, 0)
    lamp_h = 3
    lamp_location = (0, 7)
    start_state_2 = grid_robot_state(map=map, robot_location=robot_start_location, lamp_height=lamp_h,
                                     lamp_location=lamp_location)
    start_time = time.time()
    search_result_1 = search(start_state_2, base_heuristic)
    end_time = time.time() - start_time
    print("Test 3 runtime:", end_time)
    if search_result_1 is not None:
        print("Test 3 solution cost:", search_result_1[-1].g)
        print_path(search_result_1)
    else:
        print("Test 3: No path found")
# Test 2: A map with more obstacles and scattered stairs
    map_test_2 = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [-1, -1, -1, 0, 0, 0, 0, -1, -1, 0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, -1, 0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, -1, 0, 0, 0, 0, 1, 0, 0, 0, 0, -1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    robot_start_location_2 = (0, 0)
    lamp_h_2 = 4
    lamp_location_2 = (14, 0)  # bottom-left corner

    start_state_2 = grid_robot_state(map=map_test_2, robot_location=robot_start_location_2, lamp_height=lamp_h_2,
                                     lamp_location=lamp_location_2)
    start_time = time.time()
    search_result_2 = search(start_state_2, base_heuristic)
    end_time = time.time() - start_time
    print("\nTest 2 runtime:", end_time)
    if search_result_2 is not None:
        print("Test 2 solution cost:", search_result_2[-1].g)
        print_path(search_result_2)
    else:
        print("Test 2: No path found")

    # Test 3: A map with sparse obstacles and multiple small stairs
    map_test_3 = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, -1, 0, 0, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, -1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    robot_start_location_3 = (0, 0)
    lamp_h_3 = 5
    lamp_location_3 = (14, 14)

    start_state_3 = grid_robot_state(map=map_test_3, robot_location=robot_start_location_3, lamp_height=lamp_h_3,
                                     lamp_location=lamp_location_3)
    start_time = time.time()
    search_result_3 = search(start_state_3, base_heuristic)
    end_time = time.time() - start_time
    print("\nTest 3 runtime:", end_time)
    if search_result_3 is not None:
        print("Test 3 solution cost:", search_result_3[-1].g)
        print_path(search_result_3)
    else:
        print("Test 3: No path found")
