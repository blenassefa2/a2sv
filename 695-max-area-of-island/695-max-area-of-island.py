class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        m = len(grid[0])
        rank = defaultdict(int)
        root = defaultdict(tuple)
        for i in range(n):
            for j in range(m):
                rank[(i,j)] = 1
                root[(i,j)] = (i,j)
                
        
        """find function"""
        def find(a):
        
            if root[a] == a:
                return a
            root[a] = find(root[a])
            return root[a]
        
        """Union function"""
        def union(a,b):
           
            root_i, root_j = find(a), find(b)
            
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
        found = False
        Dir = [(0,1), (1,0), (-1,0), (0,-1)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    found = True
                    for d in Dir:
                        nw_r,nw_c = i + d[0], j + d[1]
                        if (0 <= nw_r < n and 0<= nw_c < m) and grid[nw_r][nw_c] == 1:
                            union((i,j),(nw_r,nw_c))
    
        max_ = -1
        if not found:
            return 0
        for i in rank:
            if rank[i] >max_:
                max_ = rank[i]
        return(max_)