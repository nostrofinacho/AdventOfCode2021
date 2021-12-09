# Advent of Code 2021
# The first puzzle of the ninth day
# ~~~~~ Smoking is harmful ~~~~~
# Modelling the smoke flow through the abandoned lava tubes


# Volcanic cave - leftover after some lava activity
class Cave:
    # Cave height map -> access height point by height_map[row][column]
    height_map = []
    low_points = []
    cave_width = 0
    cave_height = 0

    # Cave constructor
    def __init__(self, cave_generating_string):
        for line in cave_generating_string:
            self.height_map.append(list(map(int, list(line.strip()))))
            self.cave_width = len(self.height_map[0])
            self.cave_height = len(self.height_map)

    # Find the 2D coordinates of cave's low points
    def find_low_points(self):
        for row in range(self.cave_height):
            for column in range(self.cave_width):
                if self.is_low_point(row, column):
                    self.low_points.append((row, column))

    # Is cavepoint a lowpoint criteria
    def is_low_point(self, row, col):
        peers_coordinates = [(row, col-1), (row, col+1), (row-1, col), (row+1, col)]
        # Peer pressure
        for peer in peers_coordinates:
            r, c = peer
            if 0 <= r < self.cave_height and 0 <= c < self.cave_width:
                if self.height_map[row][col] >= self.height_map[r][c]:
                    return False
        return True

    # Returns the height values of low points
    def get_low_points(self):
        return [self.height_map[r][c] for r, c in self.low_points]

    # Returns the risk value of a height value
    def get_risk(self, height):
        return height + 1

    # Returns the sum of risks of all low points
    def get_total_cave_risk(self):
        return sum(list(map(self.get_risk, self.get_low_points())))


# Input parsing
with open("Day#9_Puzzle#1_Input.txt") as input_file:
    cave = Cave(input_file)

# Cave analysis
cave.find_low_points()
print("Total cave risk level:", cave.get_total_cave_risk())
