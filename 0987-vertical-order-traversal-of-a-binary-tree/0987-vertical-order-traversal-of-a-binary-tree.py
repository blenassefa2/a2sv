# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def collect(self, current,row, col):
        if not current:
            return []
        
        left = self.collect(current.left, row + 1, col -1)
        right = self.collect(current.right, row + 1, col + 1)
        
        left.extend(right)
        left.append((col, current.val, row))
        
        return left
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        lst = self.collect(root, 0,0)
        
        heapify(lst)
        answer = []
        while lst:
            
            currCol, value, row = heappop(lst)
            rows = defaultdict(list)
            rows[row].append(value)
            while lst and lst[0][0] == currCol:
                col, value, row = heappop(lst)
                rows[row].append(value)
                
            actual = []
            items = []
            for r in rows:
                items.append([r, rows[r]])
            items.sort()
            for row, values in items:
                actual.extend(sorted(values))
                
            answer.append(actual)
        return answer
        
        