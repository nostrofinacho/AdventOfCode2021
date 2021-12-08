# Advent of Code 2021
# The first puzzle of the eight day
# ~~~~~ SSS ~~~~~
# Decoding the seven-segment displays, counting the unique output digits


# Input parsing
with open("Day#8_Puzzle#1_Input.txt") as input_file:
    notes = [entry.strip() for entry in input_file.readlines()]

output_values = [note.split("|")[1].split() for note in notes]

# Counting
sum41 = 0
for output in output_values:
    for digit in output:
        # Searching for lengths of digits 1, 4, 7, and 8
        if len(digit) in [2, 4, 3, 7]:
            sum41 += 1

print("In the output values, digits 1, 4, 7, and 8 appeared", sum41, "times.")
