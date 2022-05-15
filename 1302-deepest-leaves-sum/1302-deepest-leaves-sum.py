# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        self.max_depth = 0
        self.total = 0
        @cache
        def dfs(root, l):
            
            if not root.right and not root.left:
                if l > self.max_depth:
                    self.max_depth = l
                    self.total = root.val 
                elif l == self.max_depth:
                    self.total += root.val
                return 
          
            if root.left:
                dfs(root.left, l + 1)
            if root.right:
                dfs(root.right, l + 1)
            return 
        dfs(root,0)
        return self.total