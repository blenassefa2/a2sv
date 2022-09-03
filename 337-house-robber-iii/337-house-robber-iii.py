# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode], dp = defaultdict(int)) -> int:
        if root in dp:
            return dp[root]
        if not root:
            return 0
        
        not_take = self.rob(root.left) + self.rob(root.right)
        
        take = root.val
        if root.left:
            take += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right:
            take += self.rob(root.right.left) +self.rob(root.right.right)
        
        dp[root] = max(not_take, take)
        return dp[root]