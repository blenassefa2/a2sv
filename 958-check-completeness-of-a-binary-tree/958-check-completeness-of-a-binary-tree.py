# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        qu = deque([root])
        
        
        while qu:
            
            N = len(qu)
            
            
            
            for i in range(N):
                node = qu.popleft()
                
                if not node and len(qu) > 0:
                    return False
                
                
                if node:
                    if not qu or (qu and (qu[-1] or (not qu[-1] and node.left))):
                        qu.append(node.left)


                    if not qu or (qu and (qu[-1] or (not qu[-1] and node.right))):
                        qu.append(node.right)
                
                
                
                
        return True