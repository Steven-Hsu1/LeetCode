# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Idea is that there is a carry bit either 0 or one from the
        last iteration. We can traverse the linked list normally and 
        add the values up
        """
        dummy = ListNode(-1)
        head = dummy
        cur1 = l1
        cur2 = l2
        carry = 0
        while cur1 and cur2:
            val = cur1.val + cur2.val + carry
            one_digit = val % 10
            if val > 9:
                carry = 1
            else:
                carry = 0
            head.next = ListNode(one_digit)
            
            head = head.next
            cur1 = cur1.next
            cur2 = cur2.next
        while cur1:
            val = cur1.val + carry
            one_digit = val % 10
            if val > 9:
                carry = 1
            else:
                carry = 0
            head.next = ListNode(one_digit)
            head = head.next
            cur1 = cur1.next
        while cur2:
            val = cur2.val + carry
            one_digit = val % 10
            if val > 9:
                carry = 1
            else:
                carry = 0
            head.next = ListNode(one_digit)
            head = head.next
            cur2 = cur2.next
        if carry > 0:
            head.next = ListNode(carry)
        return dummy.next
        