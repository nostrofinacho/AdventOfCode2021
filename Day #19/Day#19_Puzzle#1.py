# Advent of Code 2021
# ~~~~~ The beacons are lit! ~~~~~

tracer = []
for x in (1, -1):
    for y in (1, -1):
        for z in (1, -1):
            tracer.append((x, y, z, 0, 1, 2))
            tracer.append((x, y, z, 1, 2, 0))
            tracer.append((x, y, z, 2, 0, 1))
            tracer.append((x, y, z, 0, 2, 1))
            tracer.append((x, y, z, 2, 1, 0))
            tracer.append((x, y, z, 1, 0, 2))


def switch_up(scanner):
    little_mix = []
    for beacon in scanner:
        buffer = []
        for trace in tracer:
            buffer.append([trace[0] * beacon[trace[3]], trace[1] * beacon[trace[4]], trace[2] * beacon[trace[5]]])
        little_mix.append(buffer)
    return zip(*little_mix)
    mix = []
    for trace in tracer:
        buffer = []
        for beacon in scanner:
            buffer.append([trace[0] * beacon[trace[3]], trace[1] * beacon[trace[4]], trace[2] * beacon[trace[5]]])
        mix.append(buffer)
    return mix


def match(s1, s1_loc, s2):
    cnt_V = -1
    for variation in switch_up(s2):
        cnt_V += 1
        for beacon2 in variation:
            for beacon1 in s1:
                dif = (beacon2[0]-beacon1[0], beacon2[1]-beacon1[1], beacon2[2]-beacon1[2])
                cnt = 0
                for b2 in variation:
                    for b1 in s1:
                        if dif[0] == b2[0]-b1[0] and dif[1] == b2[1]-b1[1] and dif[2] == b2[2]-b1[2]:
                            #pair = (b1, b2)
                            #pair = ([-618,-824,-621], [686,422,578])
                            cnt += 1
                if cnt >= 12:
                    return dif, cnt_V
    return False


# Input parsing
with open("Day#19_Puzzle#1_Input_Example.txt") as input_data:
    # Each entry is a scanner represented by a detected beacons list
    scanners = []

    buffer = []
    for line in input_data.read().split("\n"):
        if "scanner" in line:
            continue
        elif line == '':
            scanners.append(buffer)
            buffer = []
            continue
        buffer.append(list(map(int, line.split(','))))

    # Testing area
    dif = match(scanners[0], [0,0,0], scanners[1])
    value = dif[0]
    print(dif[0], tracer[dif[1]])
    trace = tracer[dif[1]]
    print("....")

    for b in scanners[1]:
        print(-dif[0][0]+ b[0] * trace[0], -dif[0][1]+b[1] * trace[1], -dif[0][2]+b[2]* trace[2])

    #######################################################
    while True:
        a = 5
    scanners_positions = [[0, 0, 0] for _ in range(len(scanners))]
    scanners_done = [False for _ in range(len(scanners))]
    scanners_done[0] = True

    # Matching loop
    while not all(scanners_done):
        # Outer loop -> done scanner
        for i in range(len(scanners)):
            if not scanners_done[i]:
                continue

            # Inner loop -> not yet done scanner
            for j in range(len(scanners)):
                if scanners_done[j]:
                    continue

                # Mix and match
                dif = match(scanners[i], scanners[j])
                if dif:
                    value, trace = dif[0], tracer[dif[1]]
                    temp = [trace[0] * value[trace[3]], trace[1] * value[trace[4]], trace[2] * value[trace[5]]]
                    scanners_positions[j] = [scanners_positions[i][k] - temp[k] for k in (0, 1, 2)]

                    scanners_done[j] = True

    beacons = set()
    for i in range(len(scanners)):
        offset = scanners_positions[i]
        for beacon in scanners[i]:
            beacons.add(tuple([beacon[0] - offset[0], beacon[1] - offset[1], beacon[2] - offset[2]]))
    print(len(beacons))


# Returns centralised version of the beacon list
def decentralise(beacs):
    xc, yc, zc = 0, 0, 0
    for beac in beacs:
        xc, yc, zc = xc+beac[0], yc+beac[1], zc+beac[2]
    l = len(beacs)
    xc, yc, zc = xc/l, yc/l, zc/l

    # Centralised version
    return [list(map(int, [beac[0]-xc, beac[1]-yc, beac[2]-zc])) for beac in beacs]