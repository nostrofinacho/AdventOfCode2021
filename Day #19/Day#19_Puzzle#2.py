# Advent of Code 2021
# ~~~~~ The beacons are lit! ~~~~~
import collections

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
tracer = list(reversed(tracer))


def switch_up(scanner):
    little_mix = []
    for beacon in scanner:
        buffer = []
        for trace in tracer:
            buffer.append([trace[0] * beacon[trace[3]], trace[1] * beacon[trace[4]], trace[2] * beacon[trace[5]]])
        little_mix.append(buffer)
    return zip(*little_mix)


def match(s1, s2):
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
                            cnt += 1
                if cnt >= 12:
                    return dif, cnt_V
    return False


# Input parsing
with open("Day#19_Puzzle#2_Input.txt") as input_data:
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


    # Main section - matching loop
    scanners_positions = [(0, 0, 0) for _ in range(len(scanners))]
    scanners_done = [False for _ in range(len(scanners))]
    scanners_done[0] = True

    non_matching_pairs = set()
    while not all(scanners_done):
        # Outer loop -> done scanner
        for i in range(len(scanners)):
            print(collections.Counter(scanners_done))
            if not scanners_done[i]:
                continue
            # Inner loop -> not yet done scanner
            for j in range(len(scanners)):
                if scanners_done[j] or (i, j) in non_matching_pairs:
                    continue
                # Mix and match
                dif = match(scanners[i], scanners[j])
                if dif:
                    value, trace = dif[0], tracer[dif[1]]
                    scanners_positions[j] = tuple([-value[w] for w in (0, 1, 2)])

                    # Align the newfound scanner -> set the beacons to done scanner's POV
                    for w in range(len(scanners[j])):
                        beacon = scanners[j][w]
                        scanners[j][w] = [(beacon[trace[q+3]] * trace[q]) - value[q] for q in (0, 1, 2)]

                    scanners_done[j] = True
                else:
                    non_matching_pairs.add((i, j))
                    non_matching_pairs.add((j, i))

    # Task solution - counting the beacons
    bunch = set()
    for scanner in scanners:
        for beacon in scanner:
            bunch.add(tuple(beacon))
    print("In total, there are", len(bunch), "beacons.")

    # Task #2 solution - largest manhattan pair distance
    max_distance = 0
    for location_a in scanners_positions:
        for location_b in scanners_positions:
            distance = sum([abs(location_b[q] - location_a[q]) for q in (0, 1, 2)])
            max_distance = max(max_distance, distance)
    print("The largest Manhattan distance between any two scanners: " + str(max_distance) + ".")
