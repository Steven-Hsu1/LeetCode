# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        The reason we create a dummy node is that we need to return the head of the
        merged list, but if we go iteratively, we would be at the end with no way to traverse
        back so we make a dummy node that's next value is pointing to the head of the list.
        '''
        dummy = ListNode()
        curr = dummy
        while list1 and list2:
            if list1.val > list2.val:
                curr.next = list2
                list2 = list2.next
            else:
                curr.next = list1
                list1 = list1.next
            curr = curr.next

        if list1:
            curr.next = list1
        else:
            curr.next = list2
        
        return dummy.next