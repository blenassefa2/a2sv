class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        left = 0
        right = 0
        sum_ = 0
        maximum = -100000000000000
        while right < len(nums):
            
            while right < len(nums) and right - left < k:
                sum_ += nums[right]
                right += 1
           
           
            maximum = max(maximum, sum_/k)
            sum_ -= nums[left]
            left += 1
        return maximum
                