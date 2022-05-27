class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        best = 10000000000000000000000000
        for i in range(len(nums)):
            
            t = target - nums[i] 
            
            l,r = i + 1, len(nums) - 1
            
            while l < r:
                
                s = nums[l]+nums[r]
                best = min(best, s+nums[i], key = lambda x: abs(x - target))
                if s > t:
                    r -= 1
                elif s < t:
                    l += 1
                elif s == t:
                    return target
        return best
                    
                    