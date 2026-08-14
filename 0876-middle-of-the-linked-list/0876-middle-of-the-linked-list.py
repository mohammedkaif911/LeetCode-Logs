# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        speed = head
        slow = head
        while speed and speed.next:
            slow = slow.next
            speed = speed.next.next
        return slow
        