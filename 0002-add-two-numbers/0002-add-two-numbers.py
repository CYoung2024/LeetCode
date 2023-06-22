# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = cur = ListNode(0)
        carry = False
        while l1 or l2 or carry:
            total = 0
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            if carry == True:
                total += 1
                carry = False
            if total > 9:
                carry = True
                total = total - 10
            cur.next = ListNode(total)
            cur = cur.next
        return dummy.next