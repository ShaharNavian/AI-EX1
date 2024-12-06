import heapq
from search_node import search_node
from grid_robot_state import grid_robot_state

def create_open_set():
    return []


def create_closed_set():
    return set()


def add_to_open(vn, open_set):
    return heapq.heappush(open_set, (vn.f, vn))

def open_not_empty(open_set):
    return len(open_set) > 0


def get_best(open_set):
    return heapq.heappop(open_set)[1]  # Pop the best node based on f


def add_to_closed(vn, closed_set):
    closed_set.add(vn)

# returns False if curr_neighbor state not in open_set or has a lower g from the node in open_set
#remove the node with the higher g from open_set (if exists)
def duplicate_in_open(vn, open_set):
    for _, node in open_set:
        if node.state == vn.state and node.g <= vn.g:
            return True
    return False

#returns False if curr_neighbor state not in closed_set or has a lower g from the node in closed_set
#remove the node with the higher g from closed_set (if exists)
def duplicate_in_closed(vn, closed_set):
    for node in closed_set:
        if node.state == vn.state and node.g <= vn.g:
            return True
    return False#
# def duplicate_in_open(vn, open_set):
#     for _, node in open_set:
#         if node.state == vn.state and node.g <= vn.g:
#             print("Duplicate in open:", vn.state.get_state_str())
#             return True
#     return False
#
# def duplicate_in_closed(vn, closed_set):
#     is_duplicate = vn.state.get_state_str() in closed_set
#     if is_duplicate:
#         print("Duplicate in closed:", vn.state.get_state_str())
#     return is_duplicate

# helps to debug sometimes...
def print_path(path):
    for i in range(len(path)-1):
        print(f"[{path[i].state.get_state_str()}]", end=", ")
    print(path[-1].state.state_str)


def search(start_state, heuristic):

    open_set = create_open_set()
    closed_set = create_closed_set()
    start_node = search_node(start_state, 0, heuristic(start_state))
    add_to_open(start_node, open_set)
    # print("start_node", start_node.state.get_state_str())
    # print("map:", start_node.state.map)
    while open_not_empty(open_set):
        current = get_best(open_set)
        print(f"\nExpanding state: {current.state.get_state_str()} with f={current.f}")
        print("map:", current.state.map,"\n")
        if grid_robot_state.is_goal_state(current.state):
            # print("goal reached")
            # print("curr:", current.state.get_state_str())
            path = []
            while current:
                path.append(current)
                current = current.prev
            path.reverse()
            return path
        neighbors = current.get_neighbors()
        # print("current neighbors", current.get_neighbors())
        add_to_closed(current, closed_set)
        # print("closed_set", closed_set)
        for neighbor, edge_cost in neighbors:
            # print("neighbor", neighbor.get_state_str())
            curr_neighbor = search_node(neighbor, current.g + edge_cost, heuristic(neighbor), current)
            if not duplicate_in_open(curr_neighbor, open_set) and not duplicate_in_closed(curr_neighbor, closed_set):
                add_to_open(curr_neighbor, open_set)

    return None




