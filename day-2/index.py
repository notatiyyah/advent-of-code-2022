convert_moves = {
    "X": "A",
    "Y": "B",
    "Z": "C"
}

win_conditions = {
    "A": "B",
    "B": "C",
    "C": "A"
}

move_points = {
    "A": 1,
    "B": 2,
    "C": 3
}

def calculate_if_win_points(moves): # ?? Can't think of better name
    if moves[0] == moves[1]: return 3
    return 6 if moves[1] == win_conditions[moves[0]] else 0

def split_line(line):
    moves = line.strip("\n").split(" ")
    moves[1] = convert_moves[moves[1]]
    return moves

def generate_moves(line):
    moves = line.strip("\n").split(" ")
    if moves[1] == "Y": moves[1] = moves[0]
    elif moves[1] == "Z": moves[1] = win_conditions[moves[0]]
    else: moves[1] = dict([reversed(i) for i in win_conditions.items()])[moves[0]] # Not particularly happy about this lol

    return moves

def calculate_round_points(line, ver):
    moves = split_line(line) if ver == 1 else generate_moves(line)
    return calculate_if_win_points(moves) + move_points[moves[1]]

# Part 1
with open("day-2/input.txt", "r") as f:
    print(sum([calculate_round_points(line, 1) for line in f]))

# Part 2
with open("day-2/input.txt", "r") as f:
    print(sum([calculate_round_points(line, 2) for line in f]))