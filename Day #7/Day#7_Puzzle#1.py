# Advent of Code 2021
# The first puzzle of the seventh day
# ~~~~~ The Treachery of Whales ~~~~~
# Finding the optimal crab shuffle (the one that uses up the least amount of fuel)

from statistics import median

# Reading the crab intel
with open("Day#7_Puzzle#1_Input_Example.txt") as f:
    crab_positions = list(map(int, f.readline().strip().split(",")))

# The horizontal position closest to every other position -> Median
optimal_point = median(crab_positions)
print("The optimal horizontal position is:", int(optimal_point))

# The amount of fuel the crabs spend for the maneuver
fuel_consumption = sum([abs(point - optimal_point) for point in crab_positions])
print("The crabs consume", int(fuel_consumption), "for the maneuver.")
