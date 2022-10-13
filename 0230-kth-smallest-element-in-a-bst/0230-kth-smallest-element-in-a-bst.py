# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    
        self.count = 0
        self.final = -1
        def inorder(node):
            if not node:
                return 
            inorder(node.left)
            if self.count == k -1:
                self.final = node.val
                self.count += 1
                return
            self.count += 1
            inorder(node.right)
        inorder(root)
        return self.final