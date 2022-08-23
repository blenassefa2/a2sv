# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def func(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
           
            if t1.val != t2.val:
                return False
            
            corr =func(t1.right, t2.right) and func(t1.left, t2.left)
            incorr = func(t1.right, t2.left) and func(t1.left, t2.right)
            
            return corr or incorr
        return func(root1, root2)