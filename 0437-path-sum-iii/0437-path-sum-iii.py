# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def findPathCount(node, sums, cursum, target):
    if not node:
        return 0
    
    cursum += node.val
    pathcount = sums[cursum - target]
    sums[cursum] += 1
    leftPaths = findPathCount(node.left, sums, cursum, target)
    rightPaths = findPathCount(node.right, sums, cursum, target)
    pathcount += leftPaths + rightPaths 
    
    sums[cursum] -= 1
    
    return pathcount
def pathSum(root, targetSum):
    
    sums = defaultdict(int)
    sums[0] = 1
    
    return findPathCount(root, sums, 0, targetSum)

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        return pathSum(root,targetSum)