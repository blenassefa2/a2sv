class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        right = 0
        left = 0
        max_ = 0
        count = k
        while right < len(nums) :
            
            while right < len(nums) and (nums[right] or k):
                k -= abs(nums[right] - 1)
                right += 1
              
            max_ = max(max_, right - left) 
            if k < count:
                 k += abs(nums[left] - 1)      
            left += 1
            if left >= right:
                right = left
                
        return max_