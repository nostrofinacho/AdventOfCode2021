# Advent of Code 2021
# The first puzzle of the third day
# Parsing of the submarine's binary diagnostic report


# Counts the number of times a certain bit was of value '1'
bits_sum = []

# Binary number reading & parsing loop
with open("Day#3_Puzzle#1_Input.txt") as input_file:
    for line_counter, line in enumerate(input_file):
        binary_number = line.rstrip()

        # Setting the initial bit-counting array
        if line_counter == 0:
            bits_sum = list(map(int, binary_number))
            continue

        # General state -> accumulation of bits (counting the ones because binary)
        bits_sum = [eq_bit + int(bit) for (eq_bit, bit) in zip(bits_sum, binary_number)]

# Mapping to the most common bit
gamma_rate_binary = list(map(lambda x: '1' if x / line_counter > 0.5 else '0', bits_sum))

# Inverting the gamma rate
epsilon_rate_binary = [str(abs(int(gamma_bit) - 1)) for gamma_bit in gamma_rate_binary]

# Power consumption = Decimal gamma rate * Decimal epsilon rate
power_consumption = int(''.join(gamma_rate_binary), 2) * int(''.join(epsilon_rate_binary), 2)
print("The submarine's power consumption:", power_consumption)
