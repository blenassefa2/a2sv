# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        [1,2,3,null,5,null,4]
        
        final = [1,3, 4]
        qu = []
        
        
        t O(n)
        s O(1)
        """
        if not root:
            return []
        
        final = [root.val]
        
        qu = deque([root])
        
        while qu:
            
            N = len(qu)
            
            for i in range(N):
                node = qu.popleft()
                
                if node.left:
                    qu.append(node.left)
                
                if node.right:
                    qu.append(node.right)
            if qu:        
                final.append(qu[-1].val)
        
        return final
                
        