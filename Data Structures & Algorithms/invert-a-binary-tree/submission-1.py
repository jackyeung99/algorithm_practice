# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        

        if not root: 
            return None 

        q = deque([root])

        while q:
            
            node = q.popleft()

            print(node)
            
            l, r = None, None 
            if node.left:
                l = node.left
            if node.right:
                r = node.right

            node.right = l 
            node.left = r
            if l: 
                q.append(l)
            if r: 
                q.append(r)


        return root


