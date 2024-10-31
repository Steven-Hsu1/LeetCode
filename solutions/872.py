# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node, arr):
            if node == None:
                return
            dfs(node.left, arr)
            dfs(node.right, arr)
            if node.right == None and node.left == None:
                arr.append(node.val)
            return arr
        return dfs(root1, []) == dfs(root2, [])