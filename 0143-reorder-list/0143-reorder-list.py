# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = ListNode()
        speed = head
        slow = head
        while speed and speed.next:
            slow = slow.next
            speed = speed.next.next
        second = slow.next
        slow.next = None
        reverse = None
        curr = second
        while curr:
            next_temp = curr.next
            curr.next = reverse
            reverse = curr
            curr = next_temp

        

        first = head
        second = reverse
        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2


        
        

            

        


        """
        Do not return anything, modify head in-place instead.
        """
        