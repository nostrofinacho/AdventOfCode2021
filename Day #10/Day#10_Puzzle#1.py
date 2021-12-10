# Advent of Code 2021
# The first puzzle of the tenth day
# ~~~~~ Tax on Syntax ~~~~~~
# Calculating the total syntax error score for the navigation subsystem's output

from collections import deque

# Legal chunk borders -> format: closer->opener
legal_chunks = {')':'(', ']':'[', '}':'{', '>':'<'}
scores = {')':3, ']':57, '}':1197, '>':25137}


# Scores a line -> 0 if line valid or incomplete -> returns greater than 0 if illegal line
def score_me(line):
    global legal_chunks
    stack = deque()
    for char in line:
        # If an opener is read
        if char in legal_chunks.values():
            stack.append(char)

        # If a closer is read
        elif char in legal_chunks.keys():
            if legal_chunks[char] != stack.pop():
                return scores[char]
    return 0


# Input reading
with open("Day#10_Puzzle#1_Input.txt") as input_file:
    lines = [line.strip() for line in input_file]

# Task solution
total_error_score = sum([score_me(line) for line in lines])
print("Total syntax error score:", total_error_score)
