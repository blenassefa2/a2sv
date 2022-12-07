class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        if len(nums) == 1:
            return 0
        final = inf
            
        for i in range(len(nums)):
            
            curr = inf
            
            # for i + k
            max_ = max(nums[i] + k, nums[-1] - k)
            min_ = nums[0] + k
            if i + 1 < len(nums):
                min_ =  min(min_, nums[i + 1] - k)
            
            curr = min(curr, max_ - min_)
            # for i - k
            min_ =  min(nums[0] + k, nums[i] - k)
            max_ = nums[-1] - k
            if i - 1 >= 0:
                max_ = max(nums[i-1] + k,max_)
        
            curr = min(curr, max_ - min_)
            final = min(final,curr)
        return final
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        