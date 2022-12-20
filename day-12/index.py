class Node:
    
    __instances__ = []

    def __init__(self, row, col, char):
        self.row = row
        self.col = col
        self.elevation = self.__get_elevation__(char)
        self.char = char

        self.nodes = []
        self.visited = False
        self.__assign_start_and_end_nodes__(char)
        self.__instances__.append(self)
    
    def __repr__(self):
        return f"Node ({self.col},{self.row}): {self.char}, {len(self.nodes)} children nodes"
    
    def __get_elevation__(self, char):
        if char == "S":
            return ord("a")
        if char == "E":
            return ord("z")
        return ord(char)
    
    def __assign_start_and_end_nodes__(self, char):
        global start_nodes
        global end_node
        if char == "S": #or char == "a":
            # uncomment for part 2
            try:
                start_nodes.append(self)
            except:
                start_nodes = [self]
                
        if char == "E": end_node = self

    def __add_node__(self, node):
        self.nodes.append(node)

    def add_vertices(self ,b):
        if self.elevation + 1 >= b.elevation:
            self.__add_node__(b)
        if b.elevation + 1 >= self.elevation:
            b.__add_node__(self)

def generate_graph_from_line(node_row: list[Node], next_line: list[str]):
    # Create horizontal & vertical (downwards) vertices then return next line of nodes
    next_row = []
    index = 0
    for node in node_row:
        if index + 1 <= len(node_row) - 1:
            adjacent = node_row[index + 1]
            node.add_vertices(adjacent)

        below = Node(node.row + 1, node.col, next_line[node.col])
        node.add_vertices(below)
        next_row.append(below)
        
        index += 1
    return next_row

def generate_graph(filename : str):
    with open(filename, "r") as f:
        first_row = [Node(0, index, char) for index, char in enumerate(list(f.readline().strip("\n")))]
        second_line = list(f.readline().strip("\n"))
        
        prev_row = generate_graph_from_line(first_row, second_line)

        for line in f:
            prev_row = generate_graph_from_line(prev_row, list(line.strip("\n")))

def find_shortest_path_breadth_first(start_node : Node):
    start_node.distance = 0
    queue = [start_node]

    while(len(queue) > 0):
        current = queue.pop(0)
        if current.visited: continue

        current.visited = True
        for child in current.nodes:
            if child.visited: continue
            child.distance = current.distance + 1
            if child == end_node:
                return child.distance
            else:
                queue.append(child)

    # print("Oops, this isn't supposed to happen.")
    # if here, no path found

def reset_all_visited():
    for instance in Node.__instances__:
            instance.visited = False 

def main():
    distances = []
    generate_graph("day-12/input.txt")

    for start_node in start_nodes:
        reset_all_visited()
        distance = find_shortest_path_breadth_first(start_node)
        if distance != None:
            distances.append(distance)

    # print("Distances: ", distances)
    print("Shortest distance: ", min([d for d in distances if d != None]))

main()