class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        in_bound = lambda x,y: 0<=x<len(grid) and 0<=y<len(grid[0])
        Dir =[[1,0], [0,1]]
        @lru_cache()
        def recurs(row, col):
            if not in_bound(row,col):
                return 10000000000
            if row == len(grid)-1 and col == len(grid[0]) - 1:
                return grid[-1][-1]
            ans = 100000000000
            for d in Dir:
                n_r , n_c = row + d[0], col + d[1]
                
                ans = min(recurs(n_r,n_c), ans)
                
            return ans + grid[row][col]
        return recurs(0,0)