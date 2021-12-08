# Advent of Code 2021
# The second puzzle of the eight day
# ~~~~~ SSS ~~~~~
# Completely decoding the output


# Checks if the "smaller" list of characters is contained in the bigger one
def contained(bigger, smaller):
    for s in smaller:
        if s not in bigger:
            return False
    return True


# Compares if the strings produce the same digit
def all_the_same(a, b):
    if len(a) != len(b):
        return False
    if not contained(a, b):
        return False
    return True


# Decodes the output via given input
def decode(input, output):
    used_up = [True, True, True, False, False, False, False, False, False, True]
    mapping = {1: input[0], 4: input[2], 7: input[1], 8: input[9]}

    # Process of elimination
    for i in range(3, 6):
        if contained(input[i], mapping[1]):
            mapping[3] = input[i]
            used_up[i] = True

    for i in range(6, 9):
        if not contained(input[i], mapping[1]):
            mapping[6] = input[i]
            used_up[i] = True

    for i in range(3, 6):
        if contained(mapping[6], input[i]):
            mapping[5] = input[i]
            used_up[i] = True

    for i in range(3, 6):
        if not used_up[i]:
            mapping[2] = input[i]
            used_up[i] = True

    for i in range(6, 9):
        if contained(input[i], mapping[4]):
            mapping[9] = input[i]
            used_up[i] = True

    for i in range(6, 9):
        if not used_up[i]:
            mapping[0] = input[i]
            used_up[i] = True

    # Making up the output digit
    digit_string = ''
    for digit in output:
        for m in mapping:
            if all_the_same(digit, mapping[m]):
                digit_string += str(m)
                continue
    return digit_string


# Input parsing
with open("Day#8_Puzzle#2_Input.txt") as input_file:
    notes = [entry.strip() for entry in input_file.readlines()]

inputs, outputs = [], []
for note in notes:
    a, b = note.split("|")
    inputs.append(sorted(list(map(lambda x: list(x), a.split())), key=len))
    outputs.append(list(map(lambda x: list(x), b.split())))

# Decode and sum all the outputs
sum41 = 0
for i in range(len(inputs)):
    input, output = inputs[i], outputs[i]
    sum41 += int(decode(input, output))

print("All the output values added up:", sum41)
