# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        find the root create its node
        
        do the same for its left and right
        
        """
        
        p = defaultdict(int)
        i = defaultdict(int)
        
        for index in range(len(preorder)):
            p[preorder[index]] = index
            i[inorder[index]] = index
        
        def dnc(root, l, r):
            
            if  not(l <=root<= r):
                return None
            left, right = None, None
            lr, rr = root, root
            if l < root - 1:
                lr = min(range(l, root), key = lambda x: p[inorder[x]])
                left = dnc(lr,l , root - 1)
            elif l == root -1:
                left = TreeNode(inorder[l])
            if r > root + 1:
                rr = min(range(root + 1,  r +1), key = lambda x: p[inorder[x]])
            
                right = dnc(rr, root + 1, r)
            elif r == root +1:
                right = TreeNode(inorder[r])
            
            return TreeNode(inorder[root], left, right)
        return dnc(i[preorder[0]], 0, len(inorder) -1)