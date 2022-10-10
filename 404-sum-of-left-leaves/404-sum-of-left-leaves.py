# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
       
        
        def recurse(node,pos):
            if not node:
                return 0
            
            if not node.left and not node.right:
                if pos == "L":
                    return node.val
                return 0
            return recurse(node.left, 'L') + recurse(node.right, 'R')
        
        return recurse(root,'k')