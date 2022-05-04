class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        
        count = 0
        left = 0
        right = len(nums) -1
        
        while left < right:
            n = nums[left] + nums[right]
            if n == k:
                nums[left] = -1
                nums[right] = -1
                left += 1
                right -= 1
                count += 1
            elif n > k:
                right -= 1
            else:
                left += 1
        return count
        
         