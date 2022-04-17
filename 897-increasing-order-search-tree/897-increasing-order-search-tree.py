# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
   
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.ans = TreeNode()
        self.tmp = self.ans
        def increasing(r):
            if r:
                increasing(r.left)
                self.tmp.right = TreeNode(r.val)
                self.tmp = self.tmp.right
                increasing(r.right)
        increasing(root)
        return self.ans.right