# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Approach: We can go through each list and add numbers like
        normal and keep track of "carry's". Then if one of the lists
        is longer we just keep adding it to the list or if we have an
        extra carry after. This should be a O(m+n) solution.
        '''
        dummy = ListNode()
        curr = dummy
        carry = 0
        while l1 and l2:
            num = l1.val + l2.val + carry
            carry = 0
            if num > 9:
                num %= 10
                carry = 1
            node = ListNode(num)
            curr.next = node
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            num = l1.val + carry
            carry = 0
            if num > 9:
                num %= 10
                carry = 1
            node = ListNode(num)
            curr.next = node
            curr = curr.next
            l1 = l1.next
        while l2:
            num = l2.val + carry
            carry = 0
            if num > 9:
                num %= 10
                carry = 1
            node = ListNode(num)
            curr.next = node
            curr = curr.next
            l2 = l2.next
        if carry > 0:
            node = ListNode(carry)
            curr.next = node
            curr = curr.next
        return dummy.next

