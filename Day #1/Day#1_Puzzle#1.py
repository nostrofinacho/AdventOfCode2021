# Advent of Code
# The first puzzle of the first day

depth_increment_counter = 0
with open('Day#1_Puzzle#1_Input.txt') as input_file:
    # Single-depth memory
    last_depth = None

    # Depth-reading loop
    for depth in input_file:
        depth = int(depth.rstrip())

        # Depth increased? Ignoring the first entry
        if last_depth is not None and depth > last_depth:
            depth_increment_counter += 1

        # Single-depth memory update
        last_depth = depth

# Output
print(depth_increment_counter, "measurements are larger than the previous mesaurement.")