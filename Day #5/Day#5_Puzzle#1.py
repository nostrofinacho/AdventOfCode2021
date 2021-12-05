# Advent of Code 2021
# Looks like it might snow today
# The first puzzle of the fifth day

# ~~~~~ The Hydrothermal Venture Adventure ~~~~~

# Scanning the ocean floor to avoid the most dangerous areas (lots of vents)


# Checks if the reading is valid -> in this case diagonal lines are invalid (ignored)
def check_reading_validity(reading):
    if reading[0] == reading[2] or reading[1] == reading[3]:
        return True
    return False


# Updates the ocean floor state with the given vent line (only vertical and horizontal lines are expected)
def update_the_ocean_floor(ocean_floor, line):
    x1, y1, x2, y2 = line
    for y in range(min(y1, y2), max(y1, y2)+1):
        for x in range(min(x1, x2), max(x1, x2)+1):
            ocean_floor[y][x] += 1
    return ocean_floor


# Prints the ocean floor state diagram, used for diagnostics
def print_a_floor(floor):
    for row in floor:
        print(''.join(map(lambda x: str(x) if x != 0 else '.', row)))
    return


# Reading the reading
with open("Day#5_Puzzle#1_Input_Example.txt") as input_file:
    vent_lines_scan = [list(map(int, line.strip().replace("->", ",").split(','))) for line in input_file]

# Initialise the readable ocean floor - 2D array that represents the ocean floor regarding the hydrothermal vents numbers (limited to the maximum coordinates)
ocean_floor = [[0]*max([max(reading[0], reading[2])+1 for reading in vent_lines_scan]) for _ in range(max([max(reading[1], reading[3])+1 for reading in vent_lines_scan]))]

# Parsing the reading
for vent_line in vent_lines_scan:
    # Check if the reading is to be used
    if not check_reading_validity(vent_line):
        continue

    # Update the ocean floor state
    update_the_ocean_floor(ocean_floor, vent_line)

# Check how many areas are too dangerous (those having at least 2 vents)
number_of_dangerous_areas = sum(sum(i >= 2 for i in x) for x in ocean_floor)
print(number_of_dangerous_areas, "ocean floor points are dangerous.")

# Ocean floor diagram
#print_a_floor(ocean_floor)
