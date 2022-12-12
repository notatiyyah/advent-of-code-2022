from pprint import pprint

def move_head(move: list, x_coord: int, y_coord: int):
    direction = -1 if move[0] in ["L", "D"] else 1
    move_count = (int(move[1]) + 1) * direction
    
    if move[0] in ["L", "R"]:
        new_x = list(range(x_coord, x_coord + move_count, direction))[1:]
        new_y = [y_coord] * (abs(move_count) - 1)
    else:
        new_x = [x_coord] * (abs(move_count) - 1)
        new_y = list(range(y_coord, y_coord + move_count, direction))[1:]
    
    return list(zip(new_x, new_y))

def follow(new, current, coords_list):
    if new - current >= 1:
        coords_list.append(current + 1)
    elif new - current <= -1:
        coords_list.append(current - 1)
    else:
        coords_list.append(current)

def move_tail(new_coords : list[tuple], x: int, y: int):
    x_coords = [x]
    y_coords = [y]
    for x_new, y_new in new_coords:
        x = x_coords[-1]
        y = y_coords[-1]

        # only move if is not touching on either x or y axis
        if abs(x_new - x) > 1 or abs(y_new - y) > 1:
            follow(x_new, x, x_coords)
            follow(y_new, y, y_coords)
    
    return x_coords[1:], y_coords[1:]

def main():
    head_x = 0
    head_y = 0

    x_coords = [0]
    y_coords = [0]

    with open("day-9/input.txt", "r") as f:
        for line in f:
            move = line.strip("\n").split(" ")

            new_coords = move_head(move, head_x, head_y)
            head_x, head_y = new_coords[-1]

            new_x, new_y = move_tail(new_coords, x_coords[-1], y_coords[-1])
            x_coords += new_x
            y_coords += new_y

            if len(x_coords) != len(y_coords): assert "AAA"
    
    coords = set(zip(x_coords, y_coords))
    # pprint(coords)
    pprint(len(coords))

main()