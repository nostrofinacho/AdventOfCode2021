# Advent of Code 2021
# Looks like it might snow today
# The second puzzle of the fifth day

# ~~~~~ The Hydrothermal Venture Adventure ~~~~~

# Scanning the ocean floor to avoid the most dangerous areas (lots of vents)


# Updates the ocean floor state with the given vent line (only vertical, horizontal and diagonal lines are expected)
def update_the_ocean_floor(ocean_floor, line):
    x1, y1, x2, y2 = line

    # If the line is vertical or horizontal
    if x1 == x2 or y1 == y2 or not True:
        for y in range(min(y1, y2), max(y1, y2)+1):
            for x in range(min(x1, x2), max(x1, x2)+1):
                ocean_floor[y][x] += 1

    # If the line is diagonal
    else:
        x_range = list(range(x1, x2+1, 1)) if x1 < x2 else list(range(x1, x2-1, -1))
        y_range = list(range(y1, y2+1, 1)) if y1 < y2 else list(range(y1, y2-1, -1))
        for x, y in zip(x_range, y_range):
            ocean_floor[y][x] += 1
    return ocean_floor


# Prints the ocean floor state diagram, used for diagnostics
def print_a_floor(floor):
    for row in floor:
        print(''.join(map(lambda x: str(x) if x != 0 else '.', row)))
    return


# Reading the reading
with open("Day#5_Puzzle#2_Input_Example.txt") as input_file:
    vent_lines_scan = [list(map(int, line.strip().replace("->", ",").split(','))) for line in input_file]

# Initialise the readable ocean floor - 2D array that represents the ocean floor regarding the hydrothermal vents numbers (limited to the maximum coordinates)
ocean_floor = [[0]*max([max(reading[0], reading[2])+1 for reading in vent_lines_scan]) for _ in range(max([max(reading[1], reading[3])+1 for reading in vent_lines_scan]))]

# Parsing the reading
for vent_line in vent_lines_scan:
    # Update the ocean floor state
    update_the_ocean_floor(ocean_floor, vent_line)

# Check how many areas are too dangerous (those having at least 2 vents)
number_of_dangerous_areas = sum(sum(i >= 2 for i in x) for x in ocean_floor)
print(number_of_dangerous_areas, "ocean floor points are dangerous.")

# Ocean floor diagram
print_a_floor(ocean_floor)
