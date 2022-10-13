# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev = -inf
        def func(node):
            if not node :
                return True
            ans = func(node.left) 
            
            ans = ans and self.prev < node.val
            self.prev = node.val
            ans = ans and func(node.right)
            return ans
        return func(root)
    