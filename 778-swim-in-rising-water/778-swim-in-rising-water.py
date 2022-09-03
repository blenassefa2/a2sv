class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        in_bound= lambda r,c: 0 <= r < n and 0 <= c < n
        def dp(row,col,limit,visited):
            if not in_bound(row,col):
                return False
            if grid[row][col] > limit:
                return False
            if row == n-1 and col == n-1:
                return True
            
            Dir = [(0,1),(1,0),(-1,0),(0,-1)]
            ans = False
            visited.add((row,col))
            for d in Dir:
                new_r, new_c = row +d[0], col + d[1]
                
                if (new_r,new_c) not in visited:
                    ans = ans or dp(new_r,new_c,limit,visited)
            
            return ans
        
        left = 0
        right = (n*n) -1        
        best = right
        while left <= right:
            mid = (left +right)//2
            
            if not dp(0,0,mid,set()):
                left = mid + 1
            else:
                best = mid
                right = mid -1
        return best
                