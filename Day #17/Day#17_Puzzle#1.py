# Advent of Code 2021
# ~~~~~ Looking for Sootopolis ~~~~~


# p = projectile location | v = velocity  -> returns new projectile location and new velocity (1 step)
def step(p, v):
    return (p[0] + v[0], p[1] + v[1]), (max(0, v[0]-1), v[1]-1)


# Returns hit location if the projectile visits the target area (Xt x Yt), 'False' otherwise
# If it hits, also returns maximum heigth reached
def simulate_a_shot(Xt, Yt, p, v):
    max_y = p[1]
    while p[0] <= Xt[-1] and p[1] >= Yt[0]:
        p, v = step(p, v)
        max_y = max(max_y, p[1])
        if p[0] in Xt and p[1] in Yt:
            return (p[0], p[1]), max_y
    return False


# Input parsing
with open("Day#17_Puzzle#1_Input.txt") as fin:
    l = fin.readline().strip().split(' ')[2:]
    X_ = list(map(int, l[0][2:-1].split('..')))
    Y_ = list(map(int, l[1][2:].split('..')))

    # Target area axis ranges
    X_, Y_ = list(range(X_[0], X_[1])) + [X_[1]], list(range(Y_[0], Y_[1])) + [Y_[1]]
    negate_x_axis = X_[0] < 0
    X_ = [abs(x) for x in X_]


# Starting position (the yellow submarine)
S = (0, 0)

# Getting the last possible launching 'x'
sum41 = 1
xmin = 0
while sum41 <= X_[0]:
    xmin += 1
    sum41 = sum(list(range(xmin)))
xmin -= 1

# The possible x launch variables
X = (list(range(xmin, X_[-1])) + [X_[-1]])

# The heights reached
wuthering_heights = []

# Try out every parameter x
for x in X:
    y = Y_[0]
    # And probably most of the y
    while y < 1000:
        sim = simulate_a_shot(X_, Y_, S, (x, y))
        y += 1
        if sim:
            wuthering_heights.append(sim[1])
# Solution
print("The highest shot scores a height of", max(wuthering_heights))
