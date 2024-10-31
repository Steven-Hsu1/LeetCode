# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        # left = -1, right = 1
        self.longest = 0
        def longestZZ(node, direction, count):
            if node == None:
                return 0
            self.longest = max(self.longest, count)

            if node.left is not None:
                if direction != 'left':
                    longestZZ(node.left, 'left', count + 1)
                else:
                    longestZZ(node.left, 'left', 1)
            if node.right is not None:
                if direction != 'right':
                    longestZZ(node.right, 'right', count + 1)
                else:
                    longestZZ(node.right, 'right', 1)
        
        longestZZ(root, '', 0)
        return self.longest
            
