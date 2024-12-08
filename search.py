import heapq
from search_node import search_node
from grid_robot_state import grid_robot_state


def create_open_set():
    """
    Creates and initializes an empty open set as a tuple containing a heap and a dictionary.
    """
    return [], {}


def create_closed_set():
    """
    Creates and initializes an empty closed set as a dictionary.
    """
    return {}


def add_to_open(vn, open_set):
    """
    Adds a node to the open set (heap and dictionary).

    Args:
        vn: The node to add.
        open_set: A tuple (heap, dictionary).
    """
    heap, dic = open_set
    heapq.heappush(heap, vn)
    dic[vn.state] = vn


def open_not_empty(open_set):
    """
    Checks if the open set is not empty.

    Args:
        open_set: A tuple (heap, dictionary).

    Returns:
        bool: True if the heap in the open set is not empty, False otherwise.
    """
    heap, _ = open_set
    return len(heap) > 0


def get_best(open_set):
    """
    Retrieves the node with the lowest cost from the open set.

    Args:
        open_set: A tuple (heap, dictionary).

    Returns:
        The best node, or None if the open set is empty.
    """
    heap, dic = open_set
    while heap:
        node = heapq.heappop(heap)
        if node == dic.get(node.state):  # Check if the node matches the dictionary entry
            del dic[node.state]  # Remove it from the dictionary
            return node
    return None


def add_to_closed(vn, closed_set):
    """
    Adds a node to the closed set (dictionary).

    Args:
        vn: The node to add.
        closed_set: The closed set dictionary.
    """
    closed_set[vn.state] = vn


def duplicate_in_open(vn, open_set):
    """
    Checks for a duplicate in the open set and removes the existing one if its cost is higher.

    Args:
        vn: The node to check.
        open_set: A tuple (heap, dictionary).

    Returns:
        bool: True if a duplicate with a lower or equal cost exists, False otherwise.
    """
    _, dic = open_set
    if vn.state not in dic:
        return False
    if vn.g < dic[vn.state].g:
        del dic[vn.state]
        return False
    return True


def duplicate_in_closed(vn, closed_set):
    """
    Checks for a duplicate in the closed set and removes the existing one if its cost is higher.

    Args:
        vn: The node to check.
        closed_set: The closed set dictionary.

    Returns:
        bool: True if a duplicate with a lower or equal cost exists, False otherwise.
    """
    if vn.state not in closed_set:
        return False
    if vn.g < closed_set[vn.state].g:
        del closed_set[vn.state]
        return False
    return True


# helps to debug sometimes...
def print_path(path):
    for i in range(len(path) - 1):
        print(f"[{path[i].state.get_state_str()}]", end=", ")
    # print(path[-1].state.state_str)


def search(start_state, heuristic):

    open_set = create_open_set()
    closed_set = create_closed_set()
    start_node = search_node(start_state, 0, heuristic(start_state))
    add_to_open(start_node, open_set)

    while open_not_empty(open_set):

        current = get_best(open_set)

        if grid_robot_state.is_goal_state(current.state):
            path = []
            while current:
                path.append(current)
                current = current.prev
            path.reverse()
            return path

        add_to_closed(current, closed_set)

        for neighbor, edge_cost in current.get_neighbors():
            curr_neighbor = search_node(neighbor, current.g + edge_cost, heuristic(neighbor), current)
            if not duplicate_in_open(curr_neighbor, open_set) and not duplicate_in_closed(curr_neighbor, closed_set):
                add_to_open(curr_neighbor, open_set)

    return None


