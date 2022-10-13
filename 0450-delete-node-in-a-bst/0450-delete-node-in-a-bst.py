# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def find(node):
            if not node:
                return None
            
            if node.val == key:
                a = node.right
                if a:
                    while a.left:
                        a = a.left
                    a.left = node.left
                    return node.right
                else:
                    return node.left
               
                
                
            node.left = find(node.left)
            node.right = find(node.right)
            return node
        
        
            
        return find(root)
             