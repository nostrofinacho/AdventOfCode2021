# Advent of Code 2021
# ~~~~~ Polymerization ~~~~~
# Finding the optimal polymer formula
# Naive approach no longer works

from collections import Counter

# Input parsing
with open("Day#14_Puzzle#2_Input.txt") as input_file:
    polymer_template = list(input_file.readline().strip())
    input_file.readline()   # Blank line
    pair_rules = dict([tuple(line.strip().split(' -> ')) for line in input_file.readlines()])
    pairs = []
    for i in range(len(polymer_template)-1):
        pairs.append(polymer_template[i] + polymer_template[i+1])
    pairs_count = Counter(pairs)

# Polymerization -> each individual pairs generates two more pairs
for cycle in range(40):
    new_count = Counter()
    for pair in pairs_count.keys():
        child = pair_rules[pair]
        new_count[pair[0]+child] += pairs_count[pair]   # The new left-side pair
        new_count[child+pair[1]] += pairs_count[pair]   # The new right-side pair
    pairs_count = new_count

# Count the elements (only the left accomplice)
elements_count = Counter()
for pair in pairs_count.keys():
    elements_count[pair[0]] += pairs_count[pair]

# Remember to include the final right most element
elements_count[polymer_template[-1]] += 1

# Task solution
elements_count = elements_count.most_common()
dif = elements_count[0][1] - elements_count[-1][1]
print("Quantity of the least common element subtracted from the quantity of the most common element:", dif)
