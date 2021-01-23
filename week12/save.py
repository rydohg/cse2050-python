# Author: Ryan Doherty, rdoherty2019@my.fit.edu
# Course: CSE 2050, Fall 2020
# Project: Save The Manatee
"""
Save The Manatee.

Save The Manatee game.
"""
from sys import stdin, stdout, stderr
import argparse
import urllib.request
import copy


class GameData:
    """Store the important data for the game."""

    def __init__(self, game, boat_indices, manatee_index,
                 gate_index, num_hyacinths):
        """Initialize the important data for the game."""
        self.game = game
        self.boat_indices = boat_indices
        self.manatee_index = manatee_index
        self.gate_index = gate_index
        self.num_hyacinths = num_hyacinths
        self.original_num_hyacinths = copy.deepcopy(num_hyacinths)
        self.original_game = copy.deepcopy(game)
        self.score = 0
        self.game_over = False
        self.game_over_text = ""


def get_map(url):
    """Read the map string from the URL given."""
    try:
        with urllib.request.urlopen(url) as map:
            decoded_map = map.read().decode("utf-8")
            return decoded_map
    except ValueError:
        stderr.write("Inaccessible URL")
        exit(0)


def read_map(raw_map):
    """Read the map string into the GameData object."""
    boat_indices = []
    manatee_index = [0, 0]
    number_hyacinths = 0
    gate_index = [0, 0]
    indexed_map = []
    row_count = 0
    for line in raw_map.split("\n"):
        col_count = 0
        row = []
        for character in line:
            if character == "M":
                manatee_index = [row_count, col_count]
            elif character == "*":
                boat_indices.append([row_count, col_count])
            elif character == "\\":
                number_hyacinths += 1
            elif character == "G":
                gate_index = [row_count, col_count]
            row.append(character)
            col_count += 1
        indexed_map.append(row)
        row_count += 1
    boat_indices.reverse()
    return GameData(indexed_map, boat_indices, manatee_index,
                    gate_index, number_hyacinths)


def print_map():
    """Print the map."""
    for line in game.game:
        for spot in line:
            stdout.write(spot)
        stdout.write("\n")


def can_move(new_index, is_manatee=True, move=" "):
    """Return true if the boat or manatee can move to new_index."""
    if new_index[0] == -1:
        return False
    new_index_data = game.game[new_index[0]][new_index[1]]
    if new_index_data == " ":
        return True
    elif new_index_data == "." and is_manatee:
        return True
    elif new_index_data == "\\" and is_manatee:
        return True
    elif new_index_data == "O" and is_manatee:
        return True
    elif new_index_data == "*" and is_manatee:
        if move == "l" and game.game[new_index[0]][new_index[1] - 1] == " ":
            return True
        elif move == "r" and game.game[new_index[0]][new_index[1] + 1] == " ":
            return True
    else:
        return False


def get_and_attempt_move(manatee_index):
    """Read the move from stdin and attempt the move if possible."""
    move_string = stdin.readline().lower().rstrip()
    game.score -= 1
    # TODO: arrow keys
    if move_string == "w":
        return
    elif move_string == "a":
        game.game_over = True
        game.game_over_text = "quit"
        return

    new_index = [-1, -1]
    if move_string == "u":
        new_index = [manatee_index[0] - 1, manatee_index[1]]
    elif move_string == "d":
        new_index = [manatee_index[0] + 1, manatee_index[1]]
    elif move_string == "l":
        new_index = [manatee_index[0], manatee_index[1] - 1]
    elif move_string == "r":
        new_index = [manatee_index[0], manatee_index[1] + 1]

    won_game = False
    if can_move(new_index, move=move_string):
        if game.game[new_index[0]][new_index[1]] == "\\":
            if game.num_hyacinths == 1:
                game.num_hyacinths = 0
                game.game[game.gate_index[0]][game.gate_index[1]] = "O"
            game.score += 25
            game.num_hyacinths -= 1
        if game.game[new_index[0]][new_index[1]] == "O":
            game.game_over_text = "win"
            game.game_over = True
        if game.game[new_index[0]][new_index[1]] == "*":
            for i in range(len(game.boat_indices)):
                if game.boat_indices[i] == [new_index[0], new_index[1]]:
                    if move_string == "l":
                        game.boat_indices[i] = [new_index[0], new_index[1] - 1]
                    elif move_string == "r":
                        game.boat_indices[i] = [new_index[0], new_index[1] + 1]

        game.game[manatee_index[0]][manatee_index[1]] = " "
        game.game[new_index[0]][new_index[1]] = "M"
        game.manatee_index[0] = new_index[0]
        game.manatee_index[1] = new_index[1]
    return won_game


def move_boats():
    """Handle the movement of boats downstream and collisions."""
    for i in range(len(game.boat_indices)):
        boat = game.boat_indices[i]
        new_boat_index = [boat[0] + 1, boat[1]]
        boat_can_move = False
        if can_move(new_boat_index, is_manatee=False):
            boat_can_move = True
        # Try to slip if we can
        elif game.game[boat[0] + 1][boat[1]] == "*":
            # Try to slip right first like the examples
            new_boat_index = [boat[0] + 1, boat[1] + 1]
            if can_move([new_boat_index[0], new_boat_index[1]],
                        is_manatee=False):
                boat_can_move = True
            else:
                new_boat_index = [boat[0] + 1, boat[1] - 1]
                if can_move([new_boat_index[0], new_boat_index[1]],
                            is_manatee=False):
                    boat_can_move = True
        if boat_can_move:
            game.game[boat[0]][boat[1]] = " "
            game.game[new_boat_index[0]][new_boat_index[1]] = "*"
            game.boat_indices[i] = [new_boat_index[0], new_boat_index[1]]
            # Injure the manatee and end the game if the boat
            # drifts into it with momentum
            if game.game[new_boat_index[0] + 1][new_boat_index[1]] == "M":
                game.game[new_boat_index[0] + 1][new_boat_index[1]] = "W"
                game.game_over_text = "injured"
                game.game_over = True


parser = argparse.ArgumentParser(description="Save The Manatee")
parser.add_argument("--map", help="URL to map")
args = parser.parse_args()

map_string = get_map(args.map)
game = read_map(map_string)

print_map()
while not game.game_over:
    get_and_attempt_move(game.manatee_index)
    if not game.game_over:
        move_boats()
    print_map()

if game.game_over_text == "win":
    game.score += game.original_num_hyacinths * 50
elif game.game_over_text == "quit":
    game.score += game.original_num_hyacinths * 25

stdout.write(game.game_over_text + " " + str(game.score))
