# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        qu = deque([root])
        ans = []
        
        
        while qu:
            N = len(qu)
            temp =[]
            for i in range(N):
                node = qu.popleft()
                temp.append(node.val)
                
                if node.left:
                    qu.append(node.left)
                    
                if node.right:
                    qu.append(node.right)
            if temp:
                ans.append(temp)
        return (ans)
                