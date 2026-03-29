# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # two pass approach
        # first: find length of the list
        length = 0
        ptr = head
        while ptr:
            ptr = ptr.next
            length += 1
        # second: move pointer to correct position (length - n) and need to remove next node
        if length == 1:
            head = None
            return head
        ptr = head
        position = length - n - 1
        while position != 0:
            ptr = ptr.next
            position -= 1
        ptr.next = ptr.next.next
        return head
        
            
