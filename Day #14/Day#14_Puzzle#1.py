# Advent of Code 2021
# ~~~~~ Polymerization ~~~~~
# Finding the optimal polymer formula

from collections import Counter

# Input parsing
with open("Day#14_Puzzle#1_Input.txt") as input_file:
    polymer_template = list(input_file.readline().strip())
    input_file.readline()   # Blank line
    pair_rules = dict([tuple(line.strip().split(' -> ')) for line in input_file.readlines()])

# Copy the template
polymer = [char for char in polymer_template]

# Polymer generation loop
for cycle in range(10):
    new_polymer = []
    for i in range(len(polymer)-1):
        pair = polymer[i] + polymer[i+1]
        new_polymer.append(pair[0])
        new_polymer.append(pair_rules[pair])
    new_polymer.append(pair[1])
    polymer = new_polymer
# Count
cnt = Counter(polymer).most_common()

# Task solution
dif = cnt[0][1] - cnt[-1][1]
print(polymer)
print("Quantity of the least common element subtracted from the quantity of the most common element:", dif)
