# Advent of Code 2021
# ~~~~~ The Packet Racket ~~~~~

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



###################################################################################
# Testing and running


# Test literal value packet (v:6, ID:4, Value:2021, Total length:24)
p = parse_packet(to_bin_str("D2FE28"))
print("Version:", to_dec(p.V), " TypeID:", to_dec(p.T), " Value:", to_dec(p.value), " Total length:", p.total_length)
print()


# Test operator packet (v:1, ID:6, I:0, L:27, SP1:Value=10, SP2: Value=20)
p = parse_packet(to_bin_str("38006F45291200"))
print("Version:", to_dec(p.V), " TypeID:", to_dec(p.T), " I:", p.I, " L:", to_dec(p.L))
print("Children:", len(p.children))
print("Children values:", end=' ')
for child in p.children:
    print(to_dec(child.value), end=' ')
print()
print()

# Test operator packet (v:7, ID:3, I:1, L:3, SP1:Value=1, SP2: Value=2, SP3: Value=3)
p = parse_packet(to_bin_str("EE00D40C823060"))
print("Version:", to_dec(p.V), " TypeID:", to_dec(p.T), " I:", p.I, " L:", to_dec(p.L))
print("Children:", len(p.children))
print("Children values:", end=' ')
for child in p.children:
    print(to_dec(child.value), end=' ')
print()
print()

print()
print("This should be 16:", end=' ')
print(sum_the_vs(parse_packet(to_bin_str("8A004A801A8002F478"))))

print()
print("This should be 12:", end=' ')
p = parse_packet(to_bin_str("620080001611562C8802118E34"))
print(sum_the_vs(p))

print()
print("This should be 23:", end=' ')
print(sum_the_vs(parse_packet(to_bin_str("C0015000016115A2E0802F182340"))))

print()
print("This should be 31:", end=' ')
print(sum_the_vs(parse_packet(to_bin_str("A0016C880162017C3686B18A3D4780"))))


# Run the input
with open("Day#16_Puzzle#1_Input.txt") as f:
    transmission = f.read().strip()
    root_packet = parse_packet(to_bin_str(transmission))
    print("Sum of versions throughout the packet hierarchy:", sum_the_vs(root_packet))