"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        We can just do two loops. One loop will just first deep copy
        the entire linked list without the random pointer
        We can also add a lookup table at the same time
        Then we do a separate loop to populate the random pointers of
        our new head
        """
        lookup = {}

        new_head = Node(-1)
        ans_head = new_head
        current = head
        while current:
            ans_head.next = Node(current.val)
            ans_head = ans_head.next
            lookup[current] = ans_head
            current = current.next
        current = head
        ans_head = new_head.next
        while current:
            if current.random:
                ans_head.random = lookup[current.random]
            else:
                ans_head.random = None
            ans_head = ans_head.next
            current = current.next
        return new_head.next


