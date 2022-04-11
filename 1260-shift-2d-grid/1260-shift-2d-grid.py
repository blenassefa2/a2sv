class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        x = []
        n,m = len(grid[0]), len(grid)
        for i in range(m):
            for j in range(n):
                x.append([i,j,grid[i][j]])
        while k:
            for p in range(m*n):
                if x[p][1] == n - 1 and x[p][0] == m - 1:
                    x[p][1], x[p][0]= 0,0
                elif x[p][1] == n - 1:
                    x[p][0] += 1
                    x[p][1] = 0
                elif x[p][1] != n - 1:
                    x[p][1] += 1
            k -= 1
        
        # print(x)
        for a,b,c in x:
            grid[a][b] = c    
        return grid
                
        
                    
                