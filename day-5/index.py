stacks = [
    ["B", "Z", "T"],
    ["V", "H", "T", "D", "N"],
    ["B", "F", "M", "D"],
    ["T", "J", "G", "W", "V", "Q", "L"],
    ["W", "D", "G", "P", "V", "F", "Q", "M"],
    ["V", "Z", "Q", "G", "H", "F", "S"],
    ["Z", "S", "N", "R", "L", "T", "C", "W"],
    ["Z", "H", "W", "D", "J", "N", "R", "M"],
    ["M", "Q", "L", "F", "D", "S"]
]

def remove_items_from_stack(remove_index: int, amount: int):
    split_index = len(stacks[remove_index])-amount
    removed = stacks[remove_index][split_index:]
    stacks[remove_index] = stacks[remove_index][:split_index]
    return removed

def add_items_to_stack(add_index: int, items_to_add: list):
    items_to_add.reverse() # Comment this line for part 2
    stacks[add_index] += items_to_add

with open("day-5/input.txt", "r") as f:
    for line in f:
        l = line.strip("\n").split(" ")
        blocks_to_add = remove_items_from_stack(int(l[3])-1, int(l[1]))
        add_items_to_stack(int(l[5])-1, blocks_to_add)

print("".join([stack[-1] for stack in stacks]))