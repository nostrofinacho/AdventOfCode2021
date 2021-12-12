# Advent of Code
# The first puzzle of the twelfth day
# ~~~~~ The Pathfinder ~~~~~
# ~~~~~ I'll be your spotter ~~~~~

import copy, collections

# Mapping -> format is [[beggining_area, end area], [beggining_area, end area], ...]
bag_end = []
small_caves = []    # List of small caves
small_big_caves = []    # The small caves that could be visited twice


# Recreates a path into a string
def get_path(n):
    path = []
    while n[2] is not None:
        path.insert(0, n[0])
        n = n[2]
    path.insert(0, n[0])
    return ','.join(path)


# Searches for all the next possible areas, given a path
def search_around_path(path):
    # The mapping is bilateral, hence the two next-area lists
    a = [rule[1] for rule in bag_end if rule[0] == path.split(',')[-1]]
    b = [rule[0] for rule in bag_end if rule[1] == path.split(',')[-1]]
    return a + b


# Expands a node
def expand(n):
    return [[area, n[1] + 1, n, copy.deepcopy(n[3]), n[4]] for area in search_around_path(n[0]) if area not in n[3]]


# Returns list of paths
# Node format -> (area_name, path_depth, parent_node, visited_small_caves_list, big_small_cave)
def pathfinder(s0, goal, small_big_cave):
    # Current area queue
    open = [[s0, 0, None, [], '']]

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
            if n[0] == small_big_cave and n[4] == '':
                n[4] = n[0]
            else:
                n[3].append(n[0])

        # Search for nearby areas
        for m in expand(n):
            #open.append(m)     # Breadth-first search
            open.insert(0, m)   # Depth-first search
    # Return end nodes
    return closed


# Input reading
with open("Day#12_Puzzle#2_Input.txt") as input_file:
    for line in input_file:
        # Mapping
        bag_end.append(line.strip().split('-'))

        # Remember the small caves
        for area in line.strip().split('-'):
            if area.islower() and area not in small_caves:
                small_caves.append(area)
                if area != "start" and area != "end":
                    small_big_caves.append(area)

# Find the paths, and count all the paths throughout switching the small-big cave
paths = []
paths_s = []
# A legitimate small cave is once given the two-time visit
for small_big_cave in small_big_caves:
    some_paths = pathfinder("start", "end", small_big_cave)
    paths += some_paths
    # Stringing
    for path in some_paths:
        paths_s.append(get_path(path))

# Solution
print("There are", len(collections.Counter(paths_s).keys()), "possible unique paths.")
