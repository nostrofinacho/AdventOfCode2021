# Advent of Code
# The first puzzle of the twelfth day
# ~~~~~ The Pathfinder ~~~~~
# ~~~~~ I'll be your spotter ~~~~~

import copy

# Mapping -> format is [[beggining_area, end area], [beggining_area, end area], ...]
bag_end = []
small_caves = []    # List of small caves


# Recreates a path into a string
def get_path(n):
    path = []
    while n[2] is not None:
        path.insert(0, n[0])
        n = n[2]
    return ','.join(path)


# Searches for all the next possible areas, given a path
def search_around_path(path):
    # The mapping is bilateral, hence the two next-area lists
    a = [rule[1] for rule in bag_end if rule[0] == path.split(',')[-1]]
    b = [rule[0] for rule in bag_end if rule[1] == path.split(',')[-1]]
    return a + b


# Expands a node
def expand(n):
    return [(area, n[1] + 1, n, copy.deepcopy(n[3])) for area in search_around_path(n[0]) if area not in n[3]]


# Returns list of paths
# Node format -> (area_name, path_depth, parent_node, visited_small_caves_list)
def pathfinder(s0, goal):
    # Current area queue
    open = [(s0, 0, None, [])]

    # Nodes that end a path
    closed = []

    # Main loop
    while len(open) != 0:
        n = open.pop(0)
        # Check if end area
        if n[0] == goal:
            closed.append(n)
            continue

        # Remember the small cave
        if n[0] in small_caves:
            n[3].append(n[0])

        # Search for nearby areas
        for m in expand(n):
            open.append(m)

    # Return end nodes
    return closed


# Input reading
with open("Day#12_Puzzle#1_Input.txt") as input_file:
    for line in input_file:
        # Mapping
        bag_end.append(line.strip().split('-'))

        # Remember the small caves
        for area in line.strip().split('-'):
            if area.islower():
                small_caves.append(area)

# Find and print the paths
paths = pathfinder("start", "end")
for path in paths:
    print(get_path(path))

# Task solution
print("\nThere are", len(paths), "possible paths.")
