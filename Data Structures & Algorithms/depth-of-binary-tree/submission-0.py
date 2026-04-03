# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        
        def bfs(node, level):
            if not node:
                return level
            

        
            l = bfs(node.left, level + 1)
            r = bfs(node.right, level + 1)
            
            return max(l, r)
            

        return bfs(root, level = 0)