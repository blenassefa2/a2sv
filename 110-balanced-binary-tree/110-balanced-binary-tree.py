# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def b(node):
            if not node:
                return 0, True
            
            x, y =b(node.left), b(node.right)
            
            if not x[1] or not y[1]:
                return 0, False
            
            a = abs(x[0] - y[0])
            if a > 1:
                return 0, False
            return max(x[0], y[0]) + 1, True
        return b(root)[1]