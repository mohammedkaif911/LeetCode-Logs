# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        carry = 0
        while carry or l1 or l2:
            if l1:
                v1 = l1.val
            else:
                v1 = 0
            if l2:  
                v2 = l2.val
            else:
                v2 = 0
            total = v1 + v2 + carry
            digit = total % 10
            carry = total // 10
            tail.next = ListNode(digit)
            tail = tail.next
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next
        