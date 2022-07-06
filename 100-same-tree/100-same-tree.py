# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def travers(nod1, nod2):
            if not nod1 and not nod2:
                return True
            if not nod1 or not nod2:
                return False
            
            a = travers(nod1.left,nod2.left)
            ans = nod1.val == nod2.val
            b = travers(nod1.right,nod2.right)
            return ans and a and b
        
        return(travers(p,q))