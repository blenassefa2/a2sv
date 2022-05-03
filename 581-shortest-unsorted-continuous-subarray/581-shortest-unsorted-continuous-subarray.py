class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        x = sorted(nums)
        left = 0
        right = len(nums) - 1
        
        while left<= right and x[left] == nums[left]:
            left += 1
        while right >= left and x[right] == nums[right]:
            right -= 1
        return right - left + 1
    
    """
    [-1,2,3,4,5,6,10,3,2]
    
    """