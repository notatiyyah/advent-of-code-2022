previous_characters = []

with open("day-6/input.txt", "r") as f:
    datastream = f.read().strip()
    index = 0
    for char in datastream:
        if len(previous_characters) >= 4: # change to 14 for part 2
            break
        else:   
            if char in previous_characters:
                last_index = ''.join(previous_characters).rindex(char)
                previous_characters = previous_characters[last_index + 1:]

            previous_characters.append(char)
        index += 1
    print(index)
