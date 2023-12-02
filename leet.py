import math
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        if x == 0: return True
        n_digits = int(math.log10(x))+1
        n_checks = int(n_digits/2)
        for i in range(1, n_checks+1):
            if int((x % pow(10, i)/pow(10, i-1))) != int(x/(pow(10, (n_digits-i)))) % 10:
                return False
        return True

import math
class Solution:
    def isPalindrome2(self, x: int) -> bool:
        if x < 0: return False
        if x == 0: return True
        x = str(x)
        for a, b in zip(x[:len(x)//2], reversed(x[-(-len(x)//2):])):
            print(a, b)
            if a != b: return False
        return True



def a(x):
    x = str(x)
    print(x)
    print(reversed(x))
    return x == reversed(x)


def romanToInt(s: str) -> int:
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    converted_sum = 0
    mem = values[s[0]]
    for num in [values[x] for x in s[1:]]:
        converted_sum = converted_sum + mem if mem >= num else converted_sum - mem
        mem = num
    return converted_sum + mem

from collections import deque
def isValid(s: str) -> bool:
    brackets = {'(':')', '{':'}', '[':']'}
    stack = deque()
    for x in s:
        print(stack)
        if x in opening:
            stack.append(x)
        else:
            if x != stack.pop():
                return False
        print(stack, "\n")
    if len(stack) == 0:
        return True


def binary_chop(nums: list[int], target: int) -> int:
    low, mid, high = 0, (len(nums) - 1) // 2, len(nums) - 1
    while True:
        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            high = mid - 1
        else:
            low = mid + 1
        mid = low + (high - low) // 2

        if mid == low:
            if nums[high] == target:
                return high
            elif nums[low] == target:
                return low
            elif target > nums[high]:
                return high + 1
            elif target < nums[low]:
                return low
            else:
                return mid + 1


def maxSubArrayOLd(nums: list[int]) -> int:
    a, b = float('-inf'), float('+inf')
    i, j = None, None
    moving_sum = 0
    for k, x in enumerate(nums):
        moving_sum += x
        if moving_sum >= a:
            a = moving_sum
            i = k
        if 0 <= moving_sum <= b:
            b = moving_sum
            j = k
    print()
    if j == None:
        return max(nums)
    if i == j:
        return sum(nums)
    return sum(nums[j:i+1])


def maxSubArray(nums: list[int]) -> int:
    check = max(nums)
    if check < 0:
        return check

    a, b = nums[0], nums[-1]
    i, j = None, None

    moving_sum = 0
    for i_, x in enumerate(nums):
        moving_sum += x
        if moving_sum >= a:
            a = moving_sum
            i = i_

    moving_sum = 0
    for j_, x in list(enumerate(nums))[::-1]:
        moving_sum += x
        if moving_sum >= b:
            b = moving_sum
            j = j_
    print(i, j)
    if j > i:
        return sum(nums[j:]) + sum(nums[:i])
    return sum(nums[j:i+1])

a = [1, 2, 3]
a.insert(0, 5)

print(bin(int("11", base=2) + int("1", base=2))[2:])


def mySqrtt(self, x: int) -> int:
    if x == 0 or x == 1:
        return x
    best_root = float('+inf')

    perimeter = range(math.ceil((x+1) / 2))[1:]
    lo, hi = perimeter[0], perimeter[-1]
    while lo <= hi:
        if lo == hi:
            if abs(x - hi*hi) < abs(x - best_root*best_root):
                best_root = hi
        mid = lo + (hi - lo) // 2
        square = mid * mid
        if abs(x - square) < abs(x - best_root*best_root):
            best_root = mid
        if square < x:
            lo = mid + 1
        elif square > x:
            hi = mid - 1
        else:
            return mid

    if best_root*best_root > x:
        return best_root - 1
    return int(best_root)
n = 6
#print(int(sum([math.factorial(x + i) / (math.factorial(x)*math.factorial(i)) for i, x in enumerate(range(n, -1, -2))])))

def fibonacci(n):
    n += 1
    Fi = (1 + math.sqrt(5)) / 2
    fi = Fi**(-1)
    return int((Fi**n - (-fi)**n)/math.sqrt(5))
#print(fibonacci(2))


def climbStairs(self, n: int) -> int:
    n = n+1
    Fi = (1 + math.sqrt(5)) / 2
    return int(((Fi ** n) - (-Fi) ** -n) / math.sqrt(5))
#print(climbStairs(a, 6))

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def deleteDuplicates(head):
        current = head
        while current.next is not None:
            print(current.val)
            while current.val == current.next.val:
                if current.next is None:
                    break
                current.next = current.next.next
            if current.next is None or current is None:
                break
            current = current.next
        return head


a = [1, 3, 5]
b = [2, 2, 5]
a = sorted(a + b)


def merge(nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    m_ = m - 1
    n_ = n - 1
    i = m + n - 1
    while i >= 0:
        print(i, m_, n_)
        if nums1[m_] > nums2[n_]:
            nums1[i] = nums1[m_]
            m_ = max(m_ - 1, 0)
        else:
            nums1[i] = nums2[n_]
            n_ = max(n_ - 1, 0)
        i -= 1
    print(nums1)
merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def isSymmetric(root):
    def inorder_pass(node):
        nonlocal inorder_output
        if node.left is not None:
            inorder_pass(node.left)
        else:
            inorder_output.append(None)
        inorder_output.append(node.val)
        if node.right is not None:
            inorder_pass(node.right)
        else:
            inorder_output.append(None)

    inorder_output = []
    inorder_pass(root)
    if len(inorder_output) % 2 == 0:
        return False
    return inorder_output[:len(inorder_output) // 2] == inorder_output[len(inorder_output) // 2 + 1:][::-1]


# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def isSymmetric( root) -> bool:
        left_nodes = [root.left]
        right_nodes = [root.right]
        while True:
            print(left_nodes)
            print(right_nodes)
            print()
            left_values, right_values = [], []
            for node in left_nodes:
                if node is not None:
                    left_values.append(node.val)
                else:
                    left_values.append(None)
            for node in right_nodes:
                if node is not None:
                    right_values.append(node.val)
                else:
                    right_values.append(None)
            if left_values != right_values[::-1]:
                return False
            elif 0 < len(set(left_values)) <= 1 and set(left_values).pop() == None:
                return True

            new_left_nodes = []
            new_right_nodes = []
            for node in left_nodes:
                if node is None:
                    new_left_nodes.append(None)
                    new_left_nodes.append(None)
                    continue
                new_left_nodes.append(node.left)
                new_left_nodes.append(node.right)
            for node in right_nodes:
                if node is None:
                    new_right_nodes.append(None)
                    new_right_nodes.append(None)
                    continue
                new_right_nodes.append(node.left)
                new_right_nodes.append(node.right)
            left_nodes = new_left_nodes
            right_nodes = new_right_nodes




class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
def isSymmetric(root) -> bool:
    if root is None:
        return True
    stack = deque([root.left, root.right])

    while stack:
        print(stack)
        left, right = stack.popleft()
        if left is not None or right is not None:
            if left is not None and right is not None:
                if left.val != right.val:
                    return False
                stack.append((left.left, right.right))
                stack.append((right.left, left.right))
            else:
                return False
print()
a = None
#print(isSymmetric(TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3))))

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
def maxDepth(root: 'Node') -> int:
    def depth(node):
        if node is None: return 0
        return max([depth(n) for n in node.children]) + 1
    return depth(root)
#print(maxDepth(Node(1, (Node(3, (Node(5, [None]), Node(6, [None]))), Node(2, [None]), Node(4, [None])))))

import re
s = "A man, a plan, a canal: Panama"
print(s)
s = re.sub(r'\W+', '', s)
print(s.lower())
print(s)


def isPalindrome(s: str) -> bool:
    i, j = 0, len(s)-1
    while i < j:
        while not s[i].isalnum():
            i += 1
        while not s[j].isalnum():
            j -= 1
        print(s[i], s[j])
        if s[i].lower() != s[j].lower():
            return False
        i+=1
        j-=1
    return True

#print(isPalindrome("A man, a plan, a canal: Panama"))
print()
a = [2, 2, 3, 3, 4, 4, 5, 10, 10, 5, 1000]
c=([b/2 for b in a])
a = [b for b in a]
print(c)
print(sum(c))
print()
print(a)
print(sum(a))

print((sum(c) - sum(a)) **(1/2))

bitlen = len(bin(max(a))[2:])
print(bitlen)

sum = 0
for x in a:
    sum = sum^x
print(sum)