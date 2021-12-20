# Advent of Code 2021
# ~~~~~ T-ranch dip Map ~~~~~


# Uses the given enhancing algorithm (and current lights) to calculate the output value of given pixel
def parse_a_pixel(ligths, pixel, enhancer, target):
    x, y = pixel[0], pixel[1]
    stringer = ''
    for j in (y-1, y, y+1):
        for i in (x-1, x, x + 1):
            if target == '#':
                stringer += '1' if (i, j) in ligths else '0'
            else:
                stringer += '1' if (i, j) not in ligths else '0'
    return enhancer[int(stringer, 2)]


# Returns minimum and maximum coordinates of lit pixels
def get_borders(lights):
    min_x, max_x, min_y, max_y = float('inf'), float('-inf'), float('inf'), float('-inf')
    for light in lights:
        min_x, max_x = min(min_x, light[0]), max(max_x, light[0])
        min_y, max_y = min(min_y, light[1]), max(max_y, light[1])
    return (min_x, min_y), (max_x, max_y)


# Prints the image with dark borders
def show_image(ligths, target, nontarget):
    border = 0  # Dark border width
    min_pixel, max_pixel = get_borders(ligths)
    for y in range(-border + min_pixel[1], max_pixel[1]+1+border):
        line = ''
        for x in range(-border + min_pixel[0], max_pixel[0]+1+border):
            line += target if (x, y) in ligths else nontarget
        print(line)
    return


# Input parsing
with open("Day#20_Puzzle#1_Input.txt") as input_data:
    enhance_algorithm = input_data.readline().strip()
    input_data.readline()

    # Store the coordinates of lit areas
    trench_lights = set()
    for y, line in enumerate(input_data.readlines()):
        line = line.strip()
        for x, char in enumerate(list(line)):
            if char == '#':
                trench_lights.add((x, y))

    print("Input image:")
    show_image(trench_lights, '#', '.')
    print("\n" + str(len(trench_lights)) + " pixels are lit.\n")


    # CSI Enhance
    for enhance_level in range(1, 3):
        target = "#."[enhance_level % 2]
        nontarget = ".#"[enhance_level % 2]

        new_trench_ligths = set()
        border = 1  # Size of area to be checked outside of the lit area

        # Image enhancement
        min_pixel, max_pixel = get_borders(trench_lights)
        for y in range(-border + min_pixel[1], max_pixel[1] + 1 + border):
            for x in range(-border + min_pixel[0], max_pixel[0] + 1 + border):
                if parse_a_pixel(trench_lights, (x, y), enhance_algorithm, nontarget) == target:
                    new_trench_ligths.add((x, y))

        # Printing the new image
        print("\n\nEnhancement level " + str(enhance_level) + ":")
        show_image(new_trench_ligths, target, nontarget)
        print("\n" + str(len(new_trench_ligths)) + " pixels are lit.\n")

        trench_lights = new_trench_ligths

    # Task solution
    print("\n" + "-"*45 + "\n" + str(len(trench_lights)) + " pixels are lit in the resulting image.")
