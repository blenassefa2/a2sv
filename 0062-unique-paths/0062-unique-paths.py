class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        inbound = lambda x,y: 0<=x<m and 0<=y<n
        @lru_cache()
        def recurse(i,j):
            if not inbound(i,j):
                return 0
            if i == m - 1 and j == n - 1:
                return 1
            ans = 0
            for a,b in ([[1,0], [0,1]]):
                ans += recurse(a+i,b+j)
            return ans
        return recurse(0,0)
                
            