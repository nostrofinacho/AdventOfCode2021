# Advent of Code
# ~~~~~ Actor Boot Again ~~~~~

import re


def convert_to_single_coordinate(composite):
    return composite[0]-xmin + (composite[1] - ymin) * xrange + (composite[2]-zmin) * xrange * yrange





# Input parsing
with open("Day#22_Puzzle#1_Input_Example_A.txt") as input_data:
    raw = input_data.readlines()
    lines = []
    xmin, ymin, zmin = float('inf'), float('inf'), float('inf')
    xmax, ymax, zmax = float('-inf'), float('-inf'), float('-inf')

    for line in raw:
        x1, x2, y1, y2, z1, z2 = map(int, re.findall(r"-?\d+", line))
        xmin, ymin, zmin = min(xmin, x1), min(ymin, y1), min(zmin, z1)
        xmax, ymax, zmax = max(xmax, x2), max(ymax, y2), max(zmax, z2)
        lines.append([(xmin, xmax), (ymin, ymax), (zmin, zmax)])

    xrange, yrange, zrange = abs(xmax - xmin) + 1, abs(ymax - ymin) + 1, abs(zmax - zmin) + 1
    switches = [line.split()[0] for line in raw]

# Contains coordinates of the cubes that are turned on
reactor_core = []
for i in range(len(lines)):
    line = lines[i]
    switch = switches[i]
    start = convert_to_single_coordinate((line[0][0], line[1][0], line[2][0]))
    end = convert_to_single_coordinate((line[0][1], line[1][1], line[2][1]))
    current = start
    print(start)
    while current != end:
        reactor_core.append((str(switch), current, current + xrange))
        break
print(reactor_core)
