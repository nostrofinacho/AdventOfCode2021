# Advent of Code 2021
# ~~~~~ The Packet Racket ~~~~~
# The second puzzle
# !!!!! CHECK THE "hierarchy_evaluation()" FUNCTION FOR THE PUZZLE #2 SOLUTION !!!!!


# Converts binary character to hexadecimal
def to_hex(n):
    return ([str(i) for i in range(10)] + [chr(i) for i in range(ord('A'), ord('F')+1)])[sum([pow(2, i)*int(c) for i, c in enumerate(reversed(n))])]


# Converts binary character to decimal
def to_dec(n):
    return sum([pow(2, i)*int(c) for i, c in enumerate(reversed(n))])


# Converts hexadecimal character to binary
def to_bin(n):
    n = ([str(i) for i in range(10)] + [chr(i) for i in range(ord('A'), ord('F')+1)]).index(n)
    n = hex(int(n))
    return str(format(int(n, 16), '04b'))


# Converts hexadecimal string to binary string
def to_bin_str(s):
    return ''.join([to_bin(c) for c in s])


# A packet of ID=4, contains a literal value only
class LiteralValuePacket:

    def __init__(self, b_string):
        self.V = b_string[:3]       # Version
        self.T = b_string[3:6]      # Type ID
        self.value_groups = []
        for i in range(6, len(b_string), 5):
            self.value_groups.append(b_string[i:i+5])
            if b_string[i] == '0':
                break
        self.value = ''.join([group[1:] for group in self.value_groups])
        self.total_length = 6 + 5 * len(self.value_groups)  # Total packet bitlength


# A packet of ID!=4, contains subpacket(s)
class OperatorPacket:

    def __init__(self, b_string):
        self.V = b_string[:3]   # Version
        self.T = b_string[3:6]  # Type ID
        self.I = b_string[6]    # Length type ID
        self.children = []

        # Type fork: point A
        if self.I == '0':
            self.L = b_string[7:7+15]    # Number of bits belonging to subpackets
            subs_string = b_string[7+15:7+15+to_dec(self.L)]
            while len(subs_string) != 0:
                child = parse_packet(subs_string)
                subs_string = subs_string[child.total_length:]
                self.children.append(child)
            self.total_length = sum([child.total_length for child in self.children]) + 7 + 15

        # Type fork: point B
        elif self.I == '1':
            self.L = b_string[7:7+11]    # Number of subpackets
            subs_string = b_string[7+11:]
            while len(self.children) != to_dec(self.L):
                child = parse_packet(subs_string)
                subs_string = subs_string[child.total_length:]
                self.children.append(child)
            self.total_length = sum([child.total_length for child in self.children]) + 7 + 11


# Parses a string, reads the header and creates the suitable packet
def parse_packet(s):
    if to_dec(s[3:6]) == 4:
        packet = LiteralValuePacket(s)
    else:
        packet = OperatorPacket(s)
    return packet


# Sums up all the versions of all the packets in the packet tree, oh, packet tree - how lovely are thy branches!
# Give it the root, and it gives you an integer back
def sum_the_vs(root):
    if to_dec(root.T) == 4:
        return to_dec(root.V)
    sum41 = 0
    for child in root.children:
        sum41 += sum_the_vs(child)
    return sum41 + to_dec(root.V)


# Evaluates the packet hierarchy
def hierarchy_evaluation(root):
    # Product
    def prod(X):
        p = 1
        for x in X:
            p *= x
        return p

    # Returns 1 if the first subpacket is greater than the second one -> 0 otherwise
    def greta(X):
        return int("01"[X[0] > X[1]])

    # Returns 1 if the first subpacket is lesser than the second one -> 0 otherwise
    def lester(X):
        return int("01"[X[0] < X[1]])

    # Returns 1 if the first and the second packet are of equal values -> 0 otherwise
    def equa(X):
        return int("01"[X[0] == X[1]])

    ID = to_dec(root.T)     # ID that determines the packet type

    # Literal
    if ID == 4:
        return to_dec(root.value)

    # Gather the children
    children = [hierarchy_evaluation(child) for child in root.children]

    # Stereotypes
    if ID >= 4:
        ID -= 1
    # Packet types:   0     1    2    3     5       6      7
    stere_me_pere = (sum, prod, min, max, greta, lester, equa)
    return stere_me_pere[ID](children)


########################################################################################
# Input parsing & running
with open("Day#16_Puzzle#1_Input.txt") as f:
    transmission = f.read().strip()
    root_packet = parse_packet(to_bin_str(transmission))
    print("Sum of versions throughout the packet hierarchy:", sum_the_vs(root_packet))
    message_in_the_bottle = hierarchy_evaluation(root_packet)
    print("The message states:", message_in_the_bottle)
