# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.final = root
        
        def find(node):
            if not node:
                return 0
            a = find(node.left) + find(node.right)
           
            if node == p or node == q:
                a += 1

           
            if a == 2:
                self.final = node
                return -inf
            return a
        find(root)
        return self.final