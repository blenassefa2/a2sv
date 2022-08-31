class Solution:
    def rob(self, nums: List[int]) -> int:
        danger = set()
        if len(nums) < 3:
            return max(nums)
        def recurs(i, dp):
            if i in dp:
                return dp[i]
            if i >= len(nums):
                return 0
            
            if i in danger:
                return 0
            
            rob, nrob = nums[i] +recurs(i+2, dp), recurs(i + 1,dp)
            dp[i] =  max(rob,nrob)
            return dp[i]
        
        nrob = recurs(1, defaultdict(int))
        danger.add(len(nums)-1)
        rob = nums[0] + recurs(2, defaultdict(int))
        
        return max(rob,nrob)