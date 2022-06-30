class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        0. if nums.length == 1:
            return nums[0]
        1. divide array in half:
            1.2. get maxsubarray of left half
            1.3. get maxsubarray of right half
            1.4. get the central sum
            1.5. return the maximum of the above three steps 
        
        """
        if len(nums) == 1:
            return nums[0]
        
        
        middle = len(nums)//2
        
        left = self.maxSubArray(nums[:middle])
        right= self.maxSubArray(nums[middle:])
        
        sum_r = -1000000000000
        sum_l = -1000000000000
        sum_ = 0
        p = middle
        
        while p >= 0 :
            sum_ += nums[p]
            sum_r = max(sum_r, sum_)
            p -= 1

        p = middle + 1
        sum_ = 0
        while p < len(nums):
            sum_ += nums[p]
            sum_l = max(sum_, sum_l)
            p += 1
        return max(left, right, sum_r, sum_l, sum_r + sum_l)