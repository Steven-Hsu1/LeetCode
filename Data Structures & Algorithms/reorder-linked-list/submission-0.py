# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        end = slow.next
        slow.next = None
        # reverse second half
        prev = None
        while end:
            temp = end.next
            end.next = prev
            prev = end
            end = temp

        # merge
        start, end = head, prev  #this is because after reversal, end = None while prev is the actual node at the end
        while end and start:
            temp1, temp2 = start.next, end.next
            # adjust pointers for linked list
            end.next = start.next
            start.next = end
            # move start and end pointers inward
            start = temp1
            end = temp2