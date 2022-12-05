def get_line_array(line):
    return list(line.strip("\n"))

def split_line_in_two(line):
    line_array = get_line_array(line)
    half = len(line_array)//2
    return line_array[:half], line_array[half:]

def return_char_number(char):
    return ord(char) - (38 if char.isupper() else 96)

def calculate_priority(line):
    list_1, list_2 = split_line_in_two(line)
    repeated = list(set(list_1) & set(list_2))
    if len(repeated) > 1: raise Exception(f"Too many repetitions. 1: {list_1}, 2: {list_2}, intersection: {repeated}")
    return return_char_number(repeated[0])

# Part 1
with open("day-3/input.txt", "r") as f:
    print(sum([calculate_priority(line) for line in f]))

# Part 2

def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))

def calculate_group_priority(group):
    if len(group) != 3: raise Exception(f"It's not a group of three \(.__.)/ : {group}")
    line_array = [get_line_array(line) for line in group]

    repeated = list(set(line_array[0]) & set(line_array[1]) & set(line_array[2]))
    if len(repeated) > 1: raise Exception(f"Too many repetitions. Lines: {group}, intersection: {repeated}")
    return return_char_number(repeated[0])


with open("day-3/input.txt", "r") as f:
    elf_groups = f.read().split("\n")
    priorities = [calculate_group_priority(group) for group in chunker(elf_groups, 3)]
    print(sum(priorities))
