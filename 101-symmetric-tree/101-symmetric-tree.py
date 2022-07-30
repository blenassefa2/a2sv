# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def mirror(arr):
            left , right = 0, len(arr) - 1
            
            while left <= right:
                if not arr[left] and not arr[right]:
                    left += 1
                    right -= 1
                    continue
                if not arr[left] or not arr[right]:
                    return False
                if arr[left].val != arr[right].val:
                    return False
                left += 1
                right -= 1
            return True
        
        qu = deque([root])
        
        
        while qu:
            N = len(qu)
            
            if not mirror(qu):
                return False
            
            for n in range(N):
                node = qu.popleft()
                
                if node :
                    qu.append(node.left)

                    qu.append(node.right)
                    
        return True