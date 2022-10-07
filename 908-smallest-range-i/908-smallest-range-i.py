class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        n =  max(nums) - min(nums)
        
        while not (-k <= n/2 <= k):
            
            if  n / 2 > k:
                n -= 1
            elif n / 2 < -k:
                n += 1
        
        return max(nums) - min(nums) - n