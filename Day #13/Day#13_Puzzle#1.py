# Advent of Code 2021
# ~~~~~ Rita Origami ~~~~~
# ~~~~~ The Folding ~~~~~


# Counts all the dots
def dotcount(paper):
    sum41 = 0
    for row in paper:
        sum41 += sum(row)
    return sum41


# Converts the transparent paper to a printable string
def string_me(paper):
    stringer = ''
    for i in range(len(paper)):
        for j in range(len(paper[0])):
            stringer += '#' if paper[i][j] == 1 else '.'
        stringer += "\n"
    return stringer


# Folds the transparent paper
def fold(paper, axis, z):
    # Vertical fold |---|
    if axis == 'y':
        # The fold
        for row in range(z):
            for col in range(len(paper[0])):
                paper[row][col] += paper[-row-1][col]
                paper[row][col] = min(paper[row][col], 1)
        # Paper is now of lesser area
        for row in range(z+1):
            del paper[-1]

    # Horizontal fold | | |
    elif axis == 'x':
        # The fold
        for row in range(len(paper)):
            for col in range(z):
                paper[row][col] += paper[row][-col-1]
                paper[row][col] = min(paper[row][col], 1)
        # Paper is now of lesser area
        for row in range(len(paper)):
            for col in range(z+1):
                del paper[row][-1]
    return paper


# The transparent dotted paper
paper = [[]]
dots = []   # Dot coordinates

# Input parsing
with open("Day#13_Puzzle#1_Input.txt") as input_file:
    line = input_file.readline()

    # Remember the dots
    while line != '\n':
        dots.append(list(map(int, line.strip().split(','))))
        line = input_file.readline()

    # Paper dotting
    max_x, max_y = max([coord[0] for coord in dots]), max([coord[1] for coord in dots])
    paper = [[0]*(max_x+1) for _ in range(max_y+1)]
    for dot in dots:
        paper[dot[1]][dot[0]] = 1

    # Folding
    line = input_file.readline()
    fold_counter = 0
    while line != '\n' and line != '':
        fold_counter += 1
        axis, coordinate = line.strip().split(' ')[-1].split('=')
        paper = fold(paper, axis, int(coordinate))
        print(string_me(paper))
        print(dotcount(paper), "dots are visible after the " + str(fold_counter) +". fold.")
        print("-"*38, "\n")
        if fold_counter == 1:
            break
        line = input_file.readline()
