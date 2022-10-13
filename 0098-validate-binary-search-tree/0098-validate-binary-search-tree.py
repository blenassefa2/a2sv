# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode], l=-10000000000000000,r=1000000000000000) -> bool:
        if not root :
            return True
        if not (l<root.val<r):
            return False
        return self.isValidBST(root.left,l,root.val) and self.isValidBST(root.right,root.val,r)
        