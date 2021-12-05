# Advent of Code 2021
# ThE GiAnT SquID BINGO (the American version)
# ~~~~~ In too deep ~~~~~       (1.5+km)


# Bingo board
class Board:
    board_matrix = []   # Bingo board
    hit_matrix = []     # Hit/nohit matrix (same size as the board)

    def __init__(self, board_input_matrix):
        self.board_matrix = board_input_matrix
        self.hit_matrix = [[0]*5 for _ in range(5)]
        return

    # Checks if the given number is on the board
    def check_the_number(self, number):
        for i in range(0, 5):
            for j in range(0, 5):
                if self.board_matrix[i][j] == number:
                    self.hit_matrix[i][j] = 1
        return

    # Prints the board and its binary hit/nohit matrix
    def print_me_baby_one_more_time(self):
        for row in self.board_matrix:
            print(row)
        print()

        for row in self.hit_matrix:
            print(row)
        print()
        return

    # Checks if the board got the BINGO!
    def check_if_bingo(self):
        for row in self.hit_matrix:
            if all(row):
                return True
        for column in list(zip(*self.hit_matrix)):
            if all(column):
                return True
        return False

    # Scores the board (sum of all unmarked numbers multiplied by the called number)
    def score_me(self, number):
        sum41 = 0
        for i in range(0, 5):
            for j in range(0, 5):
                if self.hit_matrix[i][j] == 0:
                    sum41 += self.board_matrix[i][j]
        return sum41 * number


# Set of all boards
boardset = []

# Input parsing
with open("Day#4_Puzzle#1_Input.txt") as input_file:
    drawn_numbers = list(map(int, input_file.readline().strip().split(',')))
    boards_input = [list(map(int, line.strip().split())) for line in input_file.readlines()]

# Collecting the boards
for i in range(1, len(boards_input), 6):
    boardset.append(Board(boards_input[i:i+5]))

# BINGO loop
bingo = False
for number in drawn_numbers:
    for board in boardset:
        board.check_the_number(number)
        if board.check_if_bingo():
            final_score = board.score_me(number)
            print("BINGO!")
            print("The BINGO! called number was:", number)
            print("Final score:", final_score)
            bingo = True
            break
    if bingo:
        break

# No cigar
if not bingo:
    print("No one wins this game after all...")
