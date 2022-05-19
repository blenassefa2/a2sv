class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        in_bound = lambda x,y: 0 <= x < n and 0 <= y < m

        Dir =[[1,0],[-1,0],[0,1],[0,-1]]
        @cache
        def dfs(coord, s):
           
            
            ans = s 
            for d in Dir:
                n_x, n_y = coord[0] + d[0], coord[1] +d[1]
                
                if in_bound(n_x,n_y):
                    if matrix[n_x][n_y] > matrix[coord[0]][coord[1]]:
                        
                        ans = max(ans, 1 + dfs((n_x,n_y),s))
                        
            return ans
        a = 0
        for i in range(n):
            for j in range(m):
                a= max(a,dfs((i,j),1)) 
                    
            
        return a