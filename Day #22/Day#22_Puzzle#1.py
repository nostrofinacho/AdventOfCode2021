# Advent of Code
# ~~~~~ Actor Boot Again ~~~~~


# Turns cuboid on or off -> a cube coordinates being in the core dictionary means the cube is on (limited to -50 <= coordinate <= 50)
def switch_cuboid(core, comp, switch):
    for x in range(max(comp[0][0], -50), min(50, comp[0][1]) + 1):
        for y in range(max(comp[1][0], -50), min(50, comp[1][1]) + 1):
            for z in range(max(comp[2][0], -50), min(50, comp[2][1]) + 1):
                if switch == 'on':
                    core.add((x, y, z))
                else:
                    if (x, y, z) in core:
                        core.remove((x, y, z))


# Input parsing
with open("Day#22_Puzzle#1_Input.txt") as input_data:
    raw = input_data.readlines()
    input_lines = [list(map(lambda x: list(map(int, x[2:].split(".."))), line.strip().split()[-1].split(','))) for line in raw]
    switches = [line.split()[0] for line in raw]


# Contains coordinates of the cubes that are turned on
reactor_core = set()
for i in range(len(switches)):
    switch_cuboid(reactor_core, input_lines[i], switches[i])

# Task solution1
print(len(reactor_core), "cubes are turned on.")
