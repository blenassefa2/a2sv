# Definition for a binary tree node.
# class TreeNode:
#     def init(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def isLeaf(root):
    if root.left == None and root.right == None:
        return True
    return False
    
class Solution:
    
        
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False
        if isLeaf(root):
            targetSum -= root.val
            if targetSum == 0:
                return True
            else:
                return False
            
        targetSum -= root.val
        if root.left and self.hasPathSum(root.left,targetSum):
            return self.hasPathSum(root.left,targetSum)
        if root.right and self.hasPathSum(root.right,targetSum):
            return self.hasPathSum(root.right,targetSum)