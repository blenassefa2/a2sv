class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        def recurse(i,dp):
            if i >= len(questions):
                return 0
            if i in dp:
                return dp[i]
            dp[i] = max(questions[i][0] + recurse(i + questions[i][1] +1,dp),
                      recurse(i+1,dp))
            return dp[i]
        return recurse(0,defaultdict(int))