# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def recurs(node, a,b):
            if not node:
                return True
            ans = a < node.val < b 
            ans = ans and recurs(node.left,a,node.val)
            ans = ans and recurs(node.right, node.val, b)
            return ans
        return recurs(root, -100000000000000, 10000000000000000000)
            
            
            