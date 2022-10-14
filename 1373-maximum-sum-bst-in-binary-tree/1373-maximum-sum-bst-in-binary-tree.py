# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        store = defaultdict(bool)
        def isValid(node):
            if not node:
                return True
            
            
            l = isValid(node.left)
            r = isValid(node.right)
            
            a = node.right
            while a and a.left:
                    a = a.left
            a = a.val if a else inf
            b = node.left
            while b and b.right:
                b = b.right
            b = b.val if b else -inf
            # print(b,node.val,a)
            store[node] = (b < node.val < a) and l and r
            return store[node]
        
            
            
            
       
        presum = defaultdict()
        def clone(node,p):
            if not node:
                return None
            
            a =TreeNode(node.val)
            p[node] = a
            a.left  = clone(node.left,p)
            a.right = clone(node.right,p)
            
            return a
        def print_(node):
            if not node:
                return
            print_(node.left)
            print(node.val,end =" ")
            print_(node.right)
            
        def sumUp(node):
            if not node:
                return 0
            a = sumUp(node.left)
            b = sumUp(node.right)
            node.val += a + b
            
            return node.val

        self.max = 0
        def find(node):
            if not node:
                return
            if store[node]:
                self.max = max(self.max, presum[node].val)
                
            find(node.left)
            find(node.right)
        prefix = clone(root,presum)
        # valid = clone(root,store)
        
        # print_(valid)
        # print()
        isValid(root)
        # print_(valid)
        sumUp(prefix)
        # for i in store:
        #     print(i.val,store[i],presum[i].val)
        find(root)
        return self.max