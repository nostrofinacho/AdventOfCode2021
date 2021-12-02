# Advent of Code 2021
# The second puzzle of the second day
# Figuring out where does the submarine end up, after taking the planned course (input)
# The submarine navigation has now been rectified according to its manual

# Cumulative keeping tabs of the course
horizontal_position = 0
depth = 0
aim = 0


# Parses the command and adjusts the submarine's position -> hardcoded commands' base
def execute_a_command(direction, magnitude):
    global horizontal_position, depth, aim
    if direction == 'forward':
        horizontal_position += magnitude
        depth += aim * magnitude
    elif direction == 'up':
        aim -= magnitude
    elif direction == 'down':
        aim += magnitude
    return


# Input commands
with open("Day#2_Puzzle#2_Input.txt") as input_file:
    # Loop through individual commands
    # Example command line -> "[direction] [magnitude] -> "forward 5"
    for command_line in input_file:
        command_line_split = command_line.rstrip().split(' ')
        direction = command_line_split[0]
        magnitude = int(command_line_split[1])

        # Executes the read command
        execute_a_command(direction, magnitude)

print("Final horizontal position:", horizontal_position)
print("Final depth:", depth)
print("Final horizontal position multiplied by the depth:", horizontal_position*depth)

