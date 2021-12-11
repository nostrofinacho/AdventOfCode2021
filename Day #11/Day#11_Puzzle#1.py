# Advent of Code 2021
# The first puzzle of the eleventh day
# ~~~~~ James Bond ~~~~~~


# Grid of octopusi, fixed size of 10x10
octogrid = []

# Input parsing
with open("Day#11_Puzzle#1_Input.txt") as input_file:
    for line in input_file:
        octogrid.append(list(map(int, line.strip())))

print("Starting octogrid:")
for line in octogrid:
    print(line)
print("-"*30)

# Run the simulation
total_flash_counter = 0
for step in range(100):
    octoflashed = [[False]*10 for _ in range(10)]
    # Firstly -> every octopus gains a point of energy
    for i in range(10):
        for j in range(10):
            octogrid[i][j] += 1

    ##############################################################
    # Secondly -> flash if you can
    flash_happened = True

    # Spread the flash
    while flash_happened:
        flash_happened = False
        for i in range(10):
            for j in range(10):
                if octogrid[i][j] > 9 and not octoflashed[i][j]:
                    flash_happened = True
                    octoflashed[i][j] = True
                    for ii in range(i-1, i+2):
                        for jj in range(j-1, j+2):
                            if 0 <= ii < 10 and 0 <= jj < 10:
                                octogrid[ii][jj] += 1

    # Reset the flashed ones to 0
    for i in range(10):
        for j in range(10):
            if octogrid[i][j] > 9:
                octogrid[i][j] = 0
                total_flash_counter += 1
    ##############################################################
    # Print the step aftermath
    print("Step", str(step+1) + ":")
    for line in octogrid:
        print(line)
    print("-"*30)

# Task solution
print("A flash occcured", total_flash_counter, "times in total.")
