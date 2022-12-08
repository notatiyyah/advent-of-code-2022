from functools import reduce

# Make grid from file
tree_grid = []
with open("day-8/input.txt", "r") as f:
    tree_grid = [list(line.strip("\n")) for line in f]

def get_all_heights(row: int, col: int):
    height = int(tree_grid[row][col])
    
    x_heights = [int(x) for x in tree_grid[row]]
    left = x_heights[:col]
    right = x_heights[col+1:]
    
    y_heights = [int(x[col]) for x in tree_grid]
    top = y_heights[:row]
    bottom = y_heights[row+1:]

    return height, left, right, top, bottom
    
def is_visible(row: int, col: int):
    if (row == 0 
        or col == 0
        or row == len(tree_grid) - 1
        or col == len(tree_grid[row]) - 1):
        return True
    
    height, left, right, top, bottom = get_all_heights(row, col)
    max_heights = [max(x) for x in [left, right, top, bottom]]
    return min(max_heights) < height
    # if any cardinal direction's 'max height tree' is shorter than the target tree (i.e. none are taller)

def calculate_height_rating(height, trees):
    view_points = 0
    for tree_height in trees:
        view_points += 1
        if tree_height >= height: break
    return view_points

def calculate_scenic_store(height, left, right, top, bottom):
    left.reverse()
    top.reverse()
    
    points = [calculate_height_rating(height, x) for x in [left, right, top, bottom]]
    return reduce(lambda x, y: x*y, points)

def pt_1():
    visible_trees = 0
    for row_num in range(len(tree_grid)):
        for col_num in range(len(tree_grid[row_num])):
            if is_visible(row_num, col_num): visible_trees += 1
    print("Part 1:", visible_trees)

def pt_2():
    points = []
    for row_num in range(len(tree_grid)):
        for col_num in range(len(tree_grid[row_num])):
            height, left, right, top, bottom = get_all_heights(row_num, col_num)
            points.append(calculate_scenic_store(height, left, right, top, bottom))            
    print("Part 2:", max(points))

pt_1()
pt_2()
