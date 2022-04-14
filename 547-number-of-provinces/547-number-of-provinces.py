class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        rank = [1] *(n)
        root = [i for i in range(n)]
        
        """find function"""
        def find(x):
            if root[x] == x:
                return x
            root[x] = find(root[x])
            return root[x]
        
        """Union function"""
        def union(i,j):
            root_i, root_j = find(i), find(j)
            
            if root_i != root_j:
                if rank[root_i] >= rank[root_j]:
                    rank[root_i] += rank[root_j]
                    rank[root_j] = 0
                    
                    root[root_j] = root_i
                else:
                    rank[root_j] += rank[root_i]
                    rank[root_i] = 0
                    
                    root[root_i] = root_j
                    
                    
        """Driver code"""
        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j] == 1:
                    union(i,j)
    
        return (n - rank.count(0))