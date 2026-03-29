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
        position = length - n
        if position == 0:
            return head.next
        ptr = head
        for i in range(length - 1):
            # if next position is the node we need to remove
            if (i + 1) == position:
                ptr.next = ptr.next.next
                break
            ptr = ptr.next
        return head
        
            
