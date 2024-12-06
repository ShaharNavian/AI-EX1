from networkx.classes import neighbors
from numba.cuda.simulator.kernelapi import andlock


class grid_robot_state:
    # you can add global params

    def __init__(self, robot_location, map=None, lamp_height=-1, lamp_location=(-1, -1),staircase_height=0):
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
                cost = 1 + self.staircase_height  # Include current staircase height in cost
                #print(f"Movement to ({nx}, {ny}) with staircase height {self.staircase_height} costs {cost}")
                new_state = grid_robot_state((nx, ny), [row[:] for row in self.map], self.lamp_height,
                                             self.lamp_location,self.staircase_height)
                neighbors.append((new_state, cost))

        # Pick up stairs
        if self.map[x][y] > 0 and self.staircase_height == 0:  # Can pick up stairs only if not already holding any
            new_state = grid_robot_state(self.location, [row[:] for row in self.map], self.lamp_height,
                                         self.lamp_location,self.staircase_height)
            new_state.pick_up_stairs()
            #print(f"Picked up stairs at ({x}, {y}), new staircase height: {new_state.staircase_height}")
            neighbors.append((new_state, 1))  # Picking up stairs costs 1

        # Place stairs
        if self.staircase_height > 0 and self.map[x][y] == 0:  # Can place stairs only if holding some
            new_state = grid_robot_state(self.location, [row[:] for row in self.map], self.lamp_height,
                                         self.lamp_location,self.staircase_height)
            new_state.place_stairs()
            #print(f"Placed stairs at ({x}, {y}), map updated.")
            neighbors.append((new_state, 1))  # Placing stairs costs 1

        # Combine stairs
        if self.staircase_height > 0 and self.map[x][y] > 0:  # Combine stairs only if both conditions are met
            new_state = grid_robot_state(self.location, [row[:] for row in self.map], self.lamp_height,
                                         self.lamp_location,self.staircase_height)
            combined_height = self.staircase_height + self.map[x][y]
            if combined_height <= self.lamp_height:  # Only combine if height doesn't exceed lamp height
                new_state.combine_stairs()
                #print(f"Combined stairs at ({x}, {y}). New staircase height: {new_state.staircase_height}")
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

    def __eq__(self, other):
        return (self.location == other.location and
                self.map == other.map and
                self.lamp_height == other.lamp_height and
                self.lamp_location == other.lamp_location and
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
            # print(f"Picked up stairs at ({x}, {y}). New staircase height: {self.staircase_height}")
            # print(self.get_state_str())
            # print(self.get_map(self))

    def place_stairs(self):
        x, y = self.location
        if self.staircase_height > 0 and self.map[x][y] == 0:
            self.map[x][y] += self.staircase_height
            self.staircase_height = 0  # Reset staircase height
            # print(f"Placed stairs at ({x}, {y}). Total height at location: {self.map[x][y]}")
            # print(self.get_state_str())
            # print(self.get_map(self))

    def combine_stairs(self):
        x, y = self.location
        if self.staircase_height > 0 and self.map[x][y] > 0:
            new_height = self.staircase_height + self.map[x][y]
            self.staircase_height = new_height
            self.map[x][y] = 0
            # print(f"Combined stairs at ({x}, {y}). New staircase height: {self.staircase_height}")
            # print(self.get_state_str())
            # print(self.get_map(self))


