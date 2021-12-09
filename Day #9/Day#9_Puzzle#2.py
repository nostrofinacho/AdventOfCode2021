# Advent of Code 2021
# The second puzzle of the ninth day
# ~~~~~ The basin messin' ~~~~~~
# Finding the three most dangerous/largest basins

import numpy as np
import cv2
from collections import Counter
from math import prod

# Volcanic cave - leftover after some lava activity
height_map = []

# Input parsing
with open("Day#9_Puzzle#2_Input.txt") as input_file:
    for line in input_file:
        height_map.append(list(map(int, list(line.strip()))))

# Map extravaganza
height_map = np.asarray(height_map)
heat_map = height_map/9.0
binary_map = heat_map.astype(int)
binary_map_inverted = np.where(binary_map == 0, 1, 0).astype(np.uint8)

# Finding and labeling the basins
ret, basin_labels = cv2.connectedComponents(binary_map_inverted, connectivity=4)
basin_dictionary = Counter(list(basin_labels.flatten()))

# Eliminate the height9 antibasin
for i in range(len(height_map)):
    for j in range(len(height_map[0])):
        if height_map[i][j] == 9:
            basin_dictionary[basin_labels[i][j]] = -1
            break
    if -1 in basin_dictionary.values():
        break

# Task solution
print("There are", ret-1, "basins.")
print("The product of sizes of the three largests basins:", prod(np.asarray(basin_dictionary.most_common(3))[:,1]))

# Display
heat_map_3c = np.zeros([len(height_map), len(height_map[0]), 3])
heat_map_3c[:,:,2] = heat_map

# The red light indicates it ain't secure
cv2.namedWindow("The Cave's basins -> Red = Dangerous", cv2.WINDOW_NORMAL)
cv2.imshow("The Cave's basins -> Red = Dangerous", heat_map_3c)
cv2.waitKey()
