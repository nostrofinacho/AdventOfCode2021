# Advent of Code 2021
# ~~~~~ Snleighfish ~~~~~

import math, itertools


# A snailfish number, a pair -> has left and right child, each can be another pair or a regular number
class Pair:
    def __init__(self, string, nesting, parent, iam):
        self.nesting = nesting + 1
        self.parent = parent
        self.iam = iam

        # Check if regular number
        if len(string.split(',')) == 1:
            self.regular = True
            self.value = int(string)
            return
        else:
            self.regular = False

        # Find the split
        ss = (string[1:-1])
        c = [0, 0]
        for i in range(len(ss)):
            if ss[i] == '[':
                c[0] += 1
            elif ss[i] == ']':
                c[1] += 1
            else:
                if c[0] == c[1] and ss[i] == ',':
                    indeks_loma = i
        # Children
        left, right = ss[:indeks_loma], ss[indeks_loma+1:]

        # Split further down
        self.left_child, self.right_child = Pair(left, self.nesting, self, 'left'), Pair(right, self.nesting, self, 'right')

    # Converts the pair into string
    def string_me(self):
        stringer = ''
        if self.left_child.regular:
            stringer += '[' + str(self.left_child.value)
        else:
            stringer += '[' + self.left_child.string_me()
        stringer += ','
        if self.right_child.regular:
            stringer += str(self.right_child.value) + ']'
        else:
            stringer += self.right_child.string_me() + ']'
        return stringer

    # Returns None if there ain't no
    def first_left(self):
        if self.iam == 'right':
            temp = self.parent.left_child
        elif self.iam == 'left':
            temp = self.parent
            while temp.iam == 'left':
                temp = temp.parent
            if temp.nesting == 0:
                return None
            temp = temp.parent.left_child
        if temp.regular:
            return temp
        while not temp.right_child.regular:
            temp = temp.right_child
        return temp.right_child

    def first_right(self):
        if self.iam == 'right':
            temp = self.parent
            while temp.iam == 'right':
                temp = temp.parent
            if temp.nesting == 0:
                return None
            temp = temp.parent.right_child
        elif self.iam == 'left':
            temp = self.parent.right_child
        if temp.regular:
            return temp
        while not temp.left_child.regular:
            temp = temp.left_child
        return temp.left_child

    def explode_me(self):
        first_left_regular = self.first_left()
        if first_left_regular:
            first_left_regular.value += self.left_child.value
        first_right_regular = self.first_right()
        if first_right_regular:
            first_right_regular.value += self.right_child.value
        self.value = 0
        self.regular = True
        del self.left_child
        del self.right_child

    def find_explosion(self):
        if self.get_root().explosion_found:
            return
        if not self.regular:
            self.left_child.find_explosion()
        if self.regular:
            return
        if self.left_child.regular and self.right_child.regular and self.nesting >= 4:
            self.explode_me()
            self.get_root().explosion_found = True
        if not self.regular:
            self.right_child.find_explosion()

    def get_root(self):
        temp = self
        while temp.nesting != 0:
            temp = temp.parent
        return temp
    from math import floor, ceil

    def split_me(self):
        self.regular = False
        self.left_child = Pair(str(math.floor(self.value/2)), self.nesting, self, 'left')
        self.right_child = Pair(str(math.ceil(self.value/2)), self.nesting, self, 'right')

    def find_split(self):
        if self.get_root().split_found:
            return
        if not self.regular:
            self.left_child.find_split()
        if self.regular and self.value >= 10:
            self.split_me()
            self.get_root().split_found = True
        if not self.regular:
            self.right_child.find_split()

    def magnitude(self):
        sum41 = 0
        if self.regular:
            return self.value
        return 3*self.left_child.magnitude() + 2*self.right_child.magnitude()


# Input parsing
with open("Day#18_Puzzle#2_Input.txt") as input_data:
    numbers = [line.strip() for line in input_data.read().split("\n")[:-1]]
    pairs = list(itertools.combinations(numbers, 2))
    pairs += list((pair[1], pair[0]) for pair in pairs)     # For the non-communicative ones...

    max_sum = 0
    for pair in pairs:
        sum = Pair('[' + pair[0] + ',' + pair[1] + ']', -1, None, None)

        sum.get_root().explosion_found = True
        sum.get_root().split_found = True
        while sum.get_root().explosion_found or sum.get_root().split_found:
            sum.get_root().explosion_found = False
            sum.find_explosion()
            if sum.get_root().explosion_found:
                continue
            sum.get_root().split_found = False
            sum.find_split()
        print("Final sum:", sum.string_me())

        # Magnitude lvl.7
        mag = sum.magnitude()
        print("Final sum's magnitude:", mag)
        max_sum = max(max_sum, mag)

# Task solution
print("Maximum achievable magnitude throught the pairs:", max_sum)
