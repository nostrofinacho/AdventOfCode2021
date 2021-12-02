# Advent of Code 2021
# The second puzzle of the first day
# The summation isn't necessary as the sliding window doesn't have any memory -> also because it moves by step = 1
# Each slide of the window affects only the first and the last window's depth, so only those are compared

from collections import deque

sum_span = 3                # The sliding window's size
line_counter = 0            # Counts the number of read input lines
sum_increment_counter = 0   # Counts how many times the size of the sliding window increased consecutively
depth_queue = deque()       # Imitates the sliding window, actually saves the depth values which are to be the starting ones of the sliding window

with open("Day#1_Puzzle#2_Input.txt") as input_file:
    for depth_line in input_file:
        depth = int(depth_line.rstrip())
        depth_queue.append(depth)
        if line_counter >= sum_span:
            if depth > depth_queue.popleft():
                sum_increment_counter += 1
        line_counter += 1

print("The sum of window (sized " + str(sum_span) + "), increased", sum_increment_counter, "times.")
