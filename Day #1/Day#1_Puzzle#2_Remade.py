# Advent of Code
# The second puzzle of the first day

DEPTH_WINDOW_SIZE = 3   # Memory size


# Increment counter accross sliding window positions
depth_window_increment_counter = 0

# Sum of the depths contained in the sliding window in the previous slide iteration
previous_window_sum = None

with open('Day#1_Puzzle#2_Input.txt') as input_file:
    # Multiple-depths sliding memory
    depth_window = []

    # Initial filling of the depth window memory to the right size & setting of the initial sum
    depth_window = [int(next(input_file).rstrip()) for i in range(DEPTH_WINDOW_SIZE)]
    previous_window_sum = sum(depth_window)

    # Depth-reading loop
    for depth in input_file:
        depth = int(depth.rstrip())

        # Update the sliding window
        depth_window.pop(0)
        depth_window.append(depth)

        # Get the current window's sum
        window_sum = sum(depth_window)

        # Depth accros window increased?
        if window_sum > previous_window_sum:
            depth_window_increment_counter += 1

        # Single-depth memory update
        previous_window_sum = window_sum

# Output
print(depth_window_increment_counter, "sums are larger than the previous sum [of the sliding window].")
