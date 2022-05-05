class Solution:
    def tribonacci(self, n: int) -> int:
        def dp(x,d):
            if x == 0:
                return 0
            if x < 3:
                return 1
            if x not in d:
                d[x] = dp(x -1,d) + dp(x -2,d) +dp(x-3,d)
            return d[x]
        return dp(n,defaultdict())