# Advent of Code 2021
# ~~~~~ Chitons in Pythons ~~~~~
# Finding the optimum-cost path through a grid -> from top left to bottom right


# Input parsing -> initialising the cithons risk grid
with open("Day#15_Puzzle#1_Input_Example.txt") as input_file:
    grid = [list(map(int, list(line.strip()))) for line in input_file]
    goal_pos = (len(grid[0])-1, len(grid)-1)


# Checks if the node's position is the goal position
def is_goal(node):
    return node[0] == goal_pos


# Returns manhattan distance from the goal state (the bottom right)
def get_h(node):
    return abs(node[0][0] - goal_pos[0]) + abs(node[0][1] - goal_pos[1])


# Returns list of succesor nodes
def get_succesors(node):
    def search_around(loc):
        lit = []
        for i, j in [(loc[0]-1, loc[1]), (loc[0]+1, loc[1]), (loc[0], loc[1]-1), (loc[0], loc[1]+1)]:
            if 0 <= i < len(grid[0]) and 0 <= j < len(grid):
                lit.append((i, j))
        return lit
    return [(loc, node[1] + 1, node, node[3] + grid[loc[0]][loc[1]]) for loc in search_around(node[0])]


# Performs an A* state search
# Node format -> (grid_location, path_length, parent_node, total_path_cost)
def pathfinder(start_loc):
    open = [[start_loc, 0, None, 0]]
    closed = []
    while len(open) != 0:
        # Get next node
        node = open.pop(0)

        # Check if goal is reached -> remember the path
        if is_goal(node):
            return node
        closed.append(node)

        # Go through the succesors
        for child in get_succesors(node):
            # Check for obsolete nodes
            better = [m for m in open + closed if m[0] == child[0] and m[3] < child[3]]
            worse = [m for m in open + closed if m[0] == child[0] and m[3] >= child[3]]
            # Remove the worse ones
            for m in worse:
                if m in open:
                    open.remove(m)
                if m in closed:
                    closed.remove(m)
            # If there are no better ones -> remember this one
            if len(better) == 0:
                open.append(child)
                open = sorted(open, key=lambda x: x[3] + get_h(x), reverse=False)
    return closed


end_goal = pathfinder((0, 0))
print("Total path risk of the lowest risk path:", end_goal[3])

# Draw the path
map = [['x']*len(grid[0]) for _ in range(len(grid))]
map[0][0] = '.'
current_node = end_goal
while current_node[2]:
    map[current_node[0][0]][current_node[0][1]] = '.'
    current_node = current_node[2]
for row in map:
    for c in row:
        print(str(c), end='')
    print()
