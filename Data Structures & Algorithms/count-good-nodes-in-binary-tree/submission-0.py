# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, biggest):
            if not node:
                return 0
            res = 0
            if node.val >= biggest:
                res = 1
            biggest = max(node.val, biggest)
            res += dfs(node.left, biggest)
            res += dfs(node.right, biggest)
            return res
        return dfs(root, root.val)
        