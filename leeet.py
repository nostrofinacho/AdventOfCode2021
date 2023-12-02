x = 43261596
y = (int(bin(x)[2:][::-1] + '0'*(34-len(bin(x))), base=2))

m = (2**32-1)

print("x", x)
print("y", y)
print("m", m)
print(m - x)


#s = ([[:digit:]]\{3\}-)\{2\}[[:digit]]\{4\}

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def reverseList(head):
    if head is None or head.next is None:
        return head

    current = head
    concurrent = current.next
    while True:

        tempa_bay_florida = concurrent.next
        print(current.val)
        print(concurrent.val)
        if tempa_bay_florida is not None:
            print(tempa_bay_florida.val)
        concurrent.next = current

        if tempa_bay_florida is None:
            return concurrent
        current = concurrent
        concurrent = tempa_bay_florida


a = ListNode(1, ListNode(2, ListNode(3, None)))
a = reverseList(a)

print(a.next.next.next.val)
print()

def dup(nums, k):
    k = min(k, len(nums))
    if k == 0:
        return False
    for i in range(len(nums)):
        if nums[i] in nums[i + 1:min(i + 1 + k, len(nums))]:
            return True
    return False

a = [1,2,3,1,2,3]
k = 2
print(dup(a, k))