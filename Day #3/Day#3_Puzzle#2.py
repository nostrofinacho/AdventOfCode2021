# Advent of Code 2021
# The second puzzle of the third day
# Verification of life support rating

with open("Day#3_Puzzle#2_Input.txt") as input_data:
    database = [list(line.rstrip()) for line in input_data]


# The least common
rotated_data = list(zip(*database))
current_database = database
for bit_counter in range(0, len(database[0])):
    bitplace = rotated_data[bit_counter]
    last_least_common_bit = "01"[(lambda x: 0 if x.count('0') <= (len(current_database)/2) else 1)(bitplace)]
    current_database = list(filter(lambda x: x[bit_counter] == last_least_common_bit, current_database))
    rotated_data = list(zip(*current_database))
    if len(current_database) == 1:
        break
CO2_scrubber_rating = ''.join(current_database[0])

# The most common
rotated_data = list(zip(*database))
current_database = database
for bit_counter in range(0, len(database[0])):
    bitplace = rotated_data[bit_counter]
    last_most_common_bit = "01"[(lambda x: 1 if x.count('1') >= (len(current_database)/2) else 0)(bitplace)]
    current_database = list(filter(lambda x: x[bit_counter] == last_most_common_bit, current_database))
    rotated_data = list(zip(*current_database))
    if len(current_database) == 1:
        break
oxygen_generator_rating = ''.join(current_database[0])

life_support_rating = int(CO2_scrubber_rating, 2) * int(oxygen_generator_rating, 2)
print("Oxygen generator rating:", oxygen_generator_rating)
print("CO2 scrubber rating:", CO2_scrubber_rating)
print("Life support rating:", life_support_rating)
