# Advent of Code 2021
# The second puzzle of the tenth day
# ~~~~~~ Tax on Syntax ~~~~~
# ~~~ It has been remade ~~~
import statistics
from collections import deque

# Legal chunk borders -> format: closer->opener
legal_chunks = {')':'(', ']':'[', '}':'{', '>':'<'}
scores = {'(':1, '[':2, '{':3, '<':4}


# Checks if given line is legal
def legal(line):
    global legal_chunks
    stack = deque()
    for char in line:
        # If an opener is read
        if char in legal_chunks.values():
            stack.append(char)

        # If a closer is read
        elif char in legal_chunks.keys():
            if legal_chunks[char] != stack.pop():
                return False
    return True


# Scores a legal line and returns the fulfilled line -> 0 if line is complete
def score_me(line):
    global legal_chunks, scores
    legal_chunks_inv = {v: k for k, v in legal_chunks.items()}

    # Parsing the line
    stack = deque()
    score = 0
    for char in line:
        # If an opener is read
        if char in legal_chunks.values():
            stack.append(char)
        # If a closer is read
        elif char in legal_chunks.keys():
            stack.pop()

    # Remake the lines and score them
    while len(stack) != 0:
        the_missing_one = stack.pop()
        line += legal_chunks_inv[the_missing_one]
        score *= 5
        score += scores[the_missing_one]
    return score, line


# Input reading
with open("Day#10_Puzzle#2_Input.txt") as input_file:
    legal_lines = [line.strip() for line in input_file if legal(line.strip())]

# Remake the lines and score them
scores, remade_lines = zip(*[score_me(line) for line in legal_lines])

# Get the task solution
print("The middle score of all legal lines:", statistics.median(scores))
