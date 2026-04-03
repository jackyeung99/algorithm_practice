# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True 

        def dfs(node, counter = 0):
            if not node:
                return 0  # height of empty tree

            l = dfs(node.left)
            if l == -1:
                return -1

            r = dfs(node.right)
            if r == -1:
                return -1

            if abs(l - r) > 1:
                return -1

            return 1 + max(l, r)

            
        return dfs(root) != -1