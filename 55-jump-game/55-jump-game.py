class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        prev = 1
        start i from len(nums) - 2 to 0:
            prev = prev - nums[i] + 1
        return prev <= 0
        
        prev = 1
        [2,0,3,1,1,4]
             |
        
        """
        prev = 1
        for i in range(len(nums) - 2, -1, -1):
            if prev - nums[i] > 0:
                prev += 1
            else:
                prev = 1
            
        
        return prev < 2