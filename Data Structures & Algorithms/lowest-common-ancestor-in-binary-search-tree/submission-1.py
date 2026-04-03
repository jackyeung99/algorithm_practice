# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        


        def dfs(node):
            if not node: 
                return (False, -1) 
        
            l, l_found = dfs(node.left)
            r, r_found = dfs(node.right)

            print(node.val)
            print(l, l_found, r, r_found)
            # percolate up

            if l_found != -1:
                return (True, l_found) 
            if r_found != -1:
                return (True, r_found) 

            # LCA found 
            if node.val == p.val and (l or r):
                return (True, node)

            if node.val == q.val and (l or r):
                return (True, node)
        
            if l and r:
                return (True, node)

            # one path found 
            if node.val == p.val or node.val == q.val:
                return (True, -1)

            if l or r:
                return (True, -1)
            
            return (False, -1)


        _, is_found = dfs(root)


        if is_found:
            return is_found
        else:
            return False



        

