from pprint import pprint

ROPE_LENGTH = 2 # Set to 10 for part 2

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
    x_heads = dict(zip(range(0,ROPE_LENGTH), [0] * ROPE_LENGTH))
    y_heads = dict(zip(range(0,ROPE_LENGTH), [0] * ROPE_LENGTH))

    coords = [(0,0)]

    with open("day-9/input.txt", "r") as f:
        for line in f:
            move = line.strip("\n").split(" ")
            new_coords = move_head(move, x_heads[0], y_heads[0])
            x_heads[0], y_heads[0] = new_coords[-1]
            # move head

            for i in range(1,ROPE_LENGTH):
                new_x, new_y = move_tail(new_coords, x_heads[i], y_heads[i])
                new_coords = list(zip(new_x, new_y))
                if len(new_x): x_heads[i] = new_x[-1]
                if len(new_y): y_heads[i] = new_y[-1]
            # loop through each knot's movements
            # update new_coords each time as each knot will follow the one before

            coords += new_coords
            # add the last x,y coords to the list
    
    unique_coords = set(coords)
    # pprint(coords)
    pprint(len(unique_coords))

main()