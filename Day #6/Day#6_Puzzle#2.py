from collections import Counter

# Advent of Code 2021
# The second puzzle of the sixth day
# ~~~~~ Fish a la Exponential ~~~~~~
# Will the lanternfish achieve ocean supremacy?
# This time the fish are too exponential for the naive approach

# Fish population -> Dictionary form -> Key = Days until procreation, Value = How many fish with that many days until procreation
fish_pop = None


# Simulates a single tick of fish population evolution (a single day)
def tick_the_fish_pop():
    global fish_pop
    new_ones = fish_pop[0]
    for i in range(9):
        fish_pop[i] = fish_pop[i+1]     # Clock tick
    fish_pop[8] += new_ones             # Some new fish
    fish_pop[6] += new_ones             # Cycle reset
    return


# Parse the submarine's fishy intel
with open("Day#6_Puzzle#2_Input.txt") as input_file:
    # Count the fish for each point of procreation cycle
    fish_pop = Counter(list(map(int, input_file.readline().strip().split(','))))

    # Fill the void
    for i in range(9):
        if i not in fish_pop.keys():
            fish_pop[i] = 0

# Simulate the fish population evolution
number_of_days = 256
for i in range(number_of_days):
    tick_the_fish_pop()

# Result of prediction -> sum of fish throughout all cycle points
print("After", number_of_days, "days there should be about", sum(fish_pop.values()), "lanternfish.")
