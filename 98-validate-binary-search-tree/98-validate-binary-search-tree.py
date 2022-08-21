# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode],a =-100000000000000, b = 10000000000000000000) -> bool:
        
        if not root:
            return True
        ans = a < root.val < b 
        ans = ans and self.isValidBST(root.left,a,root.val)
        ans = ans and self.isValidBST(root.right, root.val, b)
        return ans
       
            
            
            