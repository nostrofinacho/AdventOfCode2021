# Advent of Code
# ~~~~~ The Deep Sea Salad ~~~~~


def printout():
    stringer = ''
    for y in range(column_height):
        for x in range(line_length):
            if (x, y) in to_east:
                stringer += '>'
            elif (x, y) in to_south:
                stringer += 'v'
            elif (x, y) in nada:
                stringer += '.'
        stringer += "\n"
    print(stringer)



def move_east():
    moveable = set()
    for x, y in to_east:
        if ((x + 1) % line_length, y) in nada:
            moveable.add((x, y))
    for x, y in moveable:
        nada.add((x, y))
        to_east.remove((x, y))

        to_east.add(((x + 1) % line_length, y))
        nada.remove(((x + 1) % line_length, y))
    if len(moveable) == 0:
        return False
    return True


def move_south():
    moveable = set()
    for x, y in to_south:
        if (x, (y + 1) % column_height) in nada:
            moveable.add((x, y))
    for x, y in moveable:
        nada.add((x, y))
        to_south.remove((x, y))

        to_south.add((x, (y + 1) % column_height))
        nada.remove((x, (y + 1) % column_height))
    if len(moveable) == 0:
        return False
    return True


with open("Day#25_Puzzle#1_Input.txt") as input_file:
    to_east = set()
    to_south = set()
    nada = set()

    x, y = 0, 0


    line = input_file.readline().strip()
    line_length = len(line)
    column_height = 0
    while line:
        x = 0
        for i in range(line_length):
            if line[i] == '>':
                to_east.add((x, y))
            elif line[i] == 'v':
                to_south.add((x, y))
            else:
                nada.add((x, y))
            x += 1
        y += 1
        column_height += 1
        line = input_file.readline().strip()

    printout()

    # Main loop
    far_east_movement, south_movement = True, True
    cnt = 0
    while far_east_movement or south_movement:
        far_east_movement = move_east()
        south_movement = move_south()
        cnt += 1
        print(cnt)
        printout()

    print("First no sea-cucumber movement step is:", cnt)
