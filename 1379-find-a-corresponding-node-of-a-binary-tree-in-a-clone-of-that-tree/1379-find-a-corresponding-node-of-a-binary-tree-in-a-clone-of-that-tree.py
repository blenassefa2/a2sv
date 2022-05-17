# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        qu =deque([cloned])
         
        def equal(root1,root2):
            q = deque([[root1,root2]]) 
            
            while q:
                n,m = q.popleft()

                if n.val != m.val:
                    return False

                if n.left and m.left:
                    q.append([n.left,m.left])
                
                if n.right and m.right:
                    q.append([n.right, m.right])
                
            return True
        while qu:
            n = qu.popleft()
          
            
            if equal(n,target):
                return n
            
            if n.left:
                qu.append(n.left)
            if n.right:
                qu.append(n.right)
                
        