from networkx.classes import neighbors
from numba.cuda.simulator.kernelapi import andlock


class grid_robot_state:
    # you can add global params

    def __init__(self, robot_location, map=None, lamp_height=-1, lamp_location=(-1, -1), staircase_height=0):
        # you can use the init function for several purposes
        self.location = robot_location
        self.map = map
        self.lamp_height = lamp_height
        self.lamp_location = lamp_location
        self.staircase_height = staircase_height

    def get_neighbors(self):
        neighbors = []
        x, y = self.location
        deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Movement neighbors
        for dx, dy in deltas:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(self.map) and 0 <= ny < len(self.map[0]) and self.map[nx][ny] != -1:
                # No deep copy; share reference to map
                new_state = grid_robot_state((nx, ny), self.map, self.lamp_height,
                                             self.lamp_location, self.staircase_height)
                neighbors.append((new_state, 1+self.staircase_height))  # Movement costs 1 + staircase height

        # Pick up stairs
        if self.map[x][y] > 0 and self.staircase_height == 0:
            new_map = [row[:] for row in self.map]  # Partial copy
            new_map[x][y] = 0
            new_state = grid_robot_state(self.location, new_map, self.lamp_height, self.lamp_location, self.map[x][y])
            neighbors.append((new_state, 1))

        # Place stairs
        if self.staircase_height > 0 and self.map[x][y] == 0:
            new_map = [row[:] for row in self.map]
            new_map[x][y] = self.staircase_height
            new_state = grid_robot_state(self.location, new_map, self.lamp_height, self.lamp_location, 0)
            neighbors.append((new_state, 1))

        # Combine stairs
        if self.staircase_height > 0 and self.map[x][y] > 0 and self.staircase_height + self.map[x][
            y] <= self.lamp_height:  # Combine stairs only if both conditions are met
            new_state = grid_robot_state(self.location, [row[:] for row in self.map], self.lamp_height,
                                         self.lamp_location, self.staircase_height)
            new_state.combine_stairs()
            neighbors.append((new_state, 1))  # Combining stairs costs 1

        return neighbors

    @staticmethod
    def is_goal_state(_grid_robot_state):
        lamp_x, lamp_y = _grid_robot_state.lamp_location
        return (
                _grid_robot_state.location == _grid_robot_state.lamp_location and
                _grid_robot_state.map[lamp_x][lamp_y] == _grid_robot_state.lamp_height
        )
        # you can change the body of the function if you want
        # def __hash__(self):

        # you can change the body of the function if you want

    def __hash__(self):
        # Hash based on critical state attributes: location, map tuple, and staircase height
        map_tuple = tuple(tuple(row) for row in self.map)
        return hash((self.location, map_tuple, self.staircase_height))

    def __eq__(self, other):
        # Compare critical attributes
        return (self.location == other.location and
                self.map == other.map and
                self.staircase_height == other.staircase_height)

    @staticmethod
    def get_map(self):
        return self.map

    @staticmethod
    def get_stairs_locations(self):
        return [(x, y) for x in range(len(self.map)) for y in range(len(self.map[0])) if self.map[x][y] > 0]

    def get_state_str(self):
        return self.location, "staircase height:", self.staircase_height

    def __str__(self):
        return f"{self.get_state_str()}"

    def __repr__(self):
        return self.__str__()

    # you can add helper functions

    def pick_up_stairs(self):
        x, y = self.location
        if self.map[x][y] > 0 and self.staircase_height == 0:
            self.staircase_height = self.map[x][y]
            self.map[x][y] = 0  # Remove stairs from the map

    def place_stairs(self):
        x, y = self.location
        if self.staircase_height > 0 and self.map[x][y] == 0:
            self.map[x][y] += self.staircase_height
            self.staircase_height = 0  # Reset staircase height

    def combine_stairs(self):
        x, y = self.location
        if self.staircase_height > 0 and self.map[x][y] > 0:
            new_height = self.staircase_height + self.map[x][y]
            self.staircase_height = new_height
            self.map[x][y] = 0
