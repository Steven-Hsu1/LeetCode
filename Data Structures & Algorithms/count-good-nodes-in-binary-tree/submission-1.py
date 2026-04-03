# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_nodes_count = 0
        def dfs(node, biggest):
            if not node:
                return 0
            if node.val >= biggest:
                nonlocal good_nodes_count
                good_nodes_count += 1
                biggest = node.val
            dfs(node.left, biggest)
            dfs(node.right, biggest)
        
        dfs(root, root.val)
        return good_nodes_count