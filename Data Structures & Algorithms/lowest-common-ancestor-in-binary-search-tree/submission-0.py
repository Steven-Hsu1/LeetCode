# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
There are two cases: if p and q don't exist within the same subtree ie
both left or both right of the root, then the answer is always the root.
We can know this by checking if p < root < q or q < root < p.
If p and q exist within the same subtree, we generate a path from the node
to the root and the first duplicate element is our LCA.
'''
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(root, p, q):
            if max(p.val, q.val) < root.val:
                return dfs(root.left, p, q)
            elif min(p.val, q.val) > root.val:
                return dfs(root.right, p, q)
            else:
                return root
        return dfs(root, p, q)

            