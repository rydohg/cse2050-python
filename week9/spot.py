"""
Spot On.

Run DFS to find whether there is a path to
get to the goal with the correct die
orientation
"""

from sys import stdin, stdout
import copy


class GraphNode:
    """Defines a graph node."""

    def __init__(self, data):
        """Initialize visited to false and set data."""
        self.visited = False
        self.data = data


class Die:
    """Object representation of a die."""

    def __init__(self):
        """Initialize state of the die."""
        self.top = 3
        self.left = 5
        self.center = 1
        self.right = 2
        self.bottom = 4
        self.under = 6

    def roll(self, direction):
        """Define how to roll the dice."""
        if direction == "N":
            temp_top = self.top
            self.top = self.center
            self.center = self.bottom
            self.bottom = self.under
            self.under = temp_top
        if direction == "S":
            temp_bottom = self.bottom
            self.bottom = self.center
            self.center = self.top
            self.top = self.under
            self.under = temp_bottom
        if direction == "E":
            temp_right = self.right
            self.right = self.center
            self.center = self.left
            self.left = self.under
            self.under = temp_right
        if direction == "W":
            temp_left = self.left
            self.left = self.center
            self.center = self.right
            self.right = self.under
            self.under = temp_left


def up(row):
    """Error check going up."""
    return -1 if row == 0 else row - 1


def down(row, graph_size):
    """Error check going down."""
    return -1 if row + 1 == graph_size else row + 1


def left(col):
    """Error check going left."""
    return -1 if col == 0 else col - 1


def right(col, graph_size):
    """Error check going right."""
    return -1 if col + 1 == graph_size else col + 1


grid_size = int(stdin.readline())

grid = []
manatee_location = []
goal_location = []
goal = -1
for i in range(grid_size):
    row = []
    input_row = stdin.readline()
    for j in range(len(input_row)):
        col = input_row[j]
        if col != '\n':
            if col == "M":
                manatee_location.append(i)
                manatee_location.append(j)
            elif col != "." and col != "*":
                goal_location.append(i)
                goal_location.append(j)
                goal = col
            row.append(GraphNode(col))
    grid.append(row)


def dfs(row, col, die):
    """Run DFS on our grid."""
    node = grid[row][col]
    node.visited = True
    if node.data == "*":
        return
    if node.data == goal and die.center == int(goal):
        stdout.write("Yes")
        exit(0)
    if up(row) != -1:
        if not grid[up(row)][col].visited:
            new_die = copy.deepcopy(die)
            new_die.roll("S")
            dfs(up(row), col, new_die)
    if down(row, grid_size) != -1:
        if not grid[down(row, grid_size)][col].visited:
            new_die = copy.deepcopy(die)
            new_die.roll("N")
            dfs(down(row, grid_size), col, new_die)
    if left(col) != -1:
        if not grid[row][left(col)].visited:
            new_die = copy.deepcopy(die)
            new_die.roll("E")
            dfs(row, left(col), new_die)
    if right(col, grid_size) != -1:
        if not grid[row][right(col, grid_size)].visited:
            new_die = copy.deepcopy(die)
            new_die.roll("W")
            dfs(row, right(col, grid_size), new_die)


dfs(manatee_location[0], manatee_location[1], Die())
stdout.write("No")
