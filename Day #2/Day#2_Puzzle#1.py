# Advent of Code 2021
# The first puzzle of the second day
# Figuring out where does the submarine end up, after taking the planned course (input)

# Cumulative keeping tabs of the course
horizontal_position = 0
depth = 0
height = 0


# Adjusts the submarine's position
def move_the_submarine(direction, magnitude):
    global horizontal_position, depth, height
    if direction == "horizontally":
        horizontal_position += magnitude
    elif direction == "vertically":
        depth -= magnitude
        height += magnitude
    return


# Parses the command and adjusts the submarine's position -> hardcoded commands' base
def execute_a_command(direction, magnitude):
    if direction == 'forward':
        move_the_submarine("horizontally", magnitude)
    elif direction == 'up':
        move_the_submarine("vertically", magnitude)
    elif direction == 'down':
        move_the_submarine("vertically", -magnitude)
    return


# Input commands
with open("Day#2_Puzzle#1_Input_Example.txt") as input_file:
    # Loop through individual commands
    # Example command line -> "[direction] [magnitude] -> "forward 5"
    for command_line in input_file:
        command_line_split = command_line.rstrip().split(' ')
        direction = command_line_split[0]
        magnitude = int(command_line_split[1])

        # Executes the read command
        execute_a_command(direction, magnitude)

print("Final horizontal position:", horizontal_position)
print("Final depth:", depth, "Final height:", height)
print("Final horizontal position multiplied by the depth:", horizontal_position*depth)

