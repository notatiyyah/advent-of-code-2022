def get_x_changes(filename):
    x_changes = [1]
    with open(filename, "r") as f:
        for line in f:
            instruction = line.strip("\n").split(" ")
            if instruction[0] == "noop":
                x_changes += [0] # doesn't change
            else:
                x_changes += [0, int(instruction[1])]
    return x_changes

def part_1(x_values):
    signal_strengths = [point * x_values[point-1] for point in range(20,221,40)]
    print(sum(signal_strengths))

def part_2(x_values):
    char = 0
    for i in range(len(x_values)):
        isLit = abs(x_values[i] - char) <= 1
        isEndOfLine = i != 0 and (i+1) % 40 == 0
        
        print("#" if isLit else ".", end='\n' if isEndOfLine else '')
        char = 0 if isEndOfLine else char + 1 # iterate char

def main():
    x_changes = get_x_changes("day-10/input.txt")
    x_values = [sum(x_changes[:point]) for point in range(1,len(x_changes))]

    part_1(x_values)
    part_2(x_values)

main()