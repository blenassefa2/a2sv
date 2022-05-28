class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        best = 0
        
        
        for i in range(len(nums) -2, 0, -1):
            if nums[i] + nums[i -1] > nums[i + 1]:
                best = max(best, nums[i] + nums[i + 1]+ nums[i - 1])
                
        return best
            
            