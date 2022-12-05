# Part 1
calorie_counts = []

with open("day-1/input.txt", "r") as f:
    total = 0
    for line in f:
        if line == "\n":
            calorie_counts.append(total)
            total = 0
        else:
            total += int(line.strip("\n"))
    calorie_counts.append(total)

print(max(calorie_counts))

# Part 2
total_top_three = 0

for x in range (0,3):
    total_top_three += calorie_counts.pop(calorie_counts.index(max(calorie_counts)))

print(total_top_three)