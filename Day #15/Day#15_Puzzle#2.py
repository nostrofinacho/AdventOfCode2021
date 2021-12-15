# Advent of Code 2021
# ~~~~~ Chitons in Pythons ~~~~~
# Finding the optimum-cost path through a grid -> from top left to bottom right

# Input parsing -> initialising the cithons risk grid
# Defining the actual cave

with open("Day#15_Puzzle#2_Input_Example.txt") as input_file:
    temp_grid = [list(map(int, list(line.strip()))) for line in input_file]
    grid = [[0]*len(temp_grid[0])*5 for _ in range(len(temp_grid)*5)]

    # Creating the map of the whole cave
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            grid[i][j] = temp_grid[i%len(temp_grid[0])][j%len(temp_grid)] + int(i/len(temp_grid)) + int(j/len(temp_grid))
            if grid[i][j] > 9:
                grid[i][j] = grid[i][j] % 9

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
    visited = set()
    visited.add(open[0][0])
    while len(open) != 0:
        node = open.pop(0)
        if is_goal(node):
            return node
        for child in get_succesors(node):
            if child[0] not in visited:
                open.append(child)
                visited.add(child[0])
                open = sorted(open, key=lambda x: x[3], reverse=False)
    return False


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
print("Total path risk of the lowest risk path:", end_goal[3])
