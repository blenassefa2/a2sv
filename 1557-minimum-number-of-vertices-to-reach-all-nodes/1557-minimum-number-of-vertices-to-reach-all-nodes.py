class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        leaf = set()
        
        for i,j in edges:
            leaf.add(j)
          
        final = []
        for root in range(n):
            if root not in leaf:
                final.append(root)
        
        return final