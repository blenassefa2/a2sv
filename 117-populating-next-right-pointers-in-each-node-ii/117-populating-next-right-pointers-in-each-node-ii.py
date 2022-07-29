"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        qu = deque([root])
        
        while qu:
            ls = deque([x for x in qu])
            
            N = len(qu)
            for i in range(N):
                a = qu.popleft()
                
                if qu and i < N - 1 :
                    a.next = qu[0]
                if a:
                    if a.left:
                        qu.append(a.left)
                    if a.right:
                        qu.append(a.right)
        return root
            