class Solution:
    dp = defaultdict()
    def isUgly(self, n: int) -> bool:
        if n <=0:
            return 0
        if n == 1:
            return True
        if n in Solution.dp:
            return Solution.dp[n]
        
        if n % 5 == 0:
            Solution.dp[n] = self.isUgly(n//5)
            return Solution.dp[n]
        if n % 3 == 0:
            Solution.dp[n] = self.isUgly(n//3)
            return Solution.dp[n]
        if n % 2 == 0:
            Solution.dp[n] = self.isUgly(n//2)
            return Solution.dp[n]
        Solution.dp[n] = False
        return False