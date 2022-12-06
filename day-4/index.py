def get_sections_list(assignment):
    return list(range(int(assignment[0]), int(assignment[1]) + 1))

def do_assigments_overlap(line, version):
    assignments = [x.split('-') for x in line.strip("\n").split(",")]

    a = get_sections_list(assignments[0])
    b = get_sections_list(assignments[1])

    total_sections_covered = list(set(a + b))
    if version == 1:
        return len(total_sections_covered) == max(len(a), len(b)) # if true then one assignment completely overlaps the other
    else:
        return len(total_sections_covered) < len(a) + len(b) # if true then one assignment at least partially overlaps the other

# Part 1
with open("day-4/input.txt", "r") as f:
    results = [do_assigments_overlap(line, 1) for line in f]
    print(sum(results))
    
# Part 2
with open("day-4/input.txt", "r") as f:
    results = [do_assigments_overlap(line, 2) for line in f]
    print(sum(results))