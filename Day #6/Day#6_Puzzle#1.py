# Advent of Code 2021
# The first puzzle of the sixth day
# ~~~~~ Fish a la Exponential ~~~~~~
# Predict the size of lanternfish population over and through the deep days

# Fish population -> each entry represents a fish -> value represents fish's number of remaining days until procreating a new fish
fish_pop = None


# Simulates a single tick of fish population evolution (a single day)
def tick_the_fish_pop():
    global fish_pop
    new_fishes = fish_pop.count(0)  # The ones to procreate
    new_fish_pop = [until_life - 1 if until_life > 0 else 6 for until_life in fish_pop]   # Ticking the clock
    for _ in range(new_fishes):
        new_fish_pop.append(8)
    fish_pop = new_fish_pop     # Generation gap


# Parse the submarine's fishy intel
with open("Day#6_Puzzle#1_Input_Example.txt") as input_file:
    fish_pop = list(map(int, input_file.readline().strip().split(',')))

# Simulate the fish population
number_of_days = 80
for i in range(number_of_days):
    tick_the_fish_pop()

# Result of prediction
print("After", number_of_days, "days there should be about", len(fish_pop), "lanternfish.")
