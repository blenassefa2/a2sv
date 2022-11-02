class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum_ = 0
        pre_sum = []
        pre_sum2 = []
        for i in nums:
            sum_ += i
            pre_sum.append(sum_)
        sum_ = 0
        for i in range(len(nums)-1, -1, -1):
            sum_ += nums[i]
            pre_sum2.append(sum_)
        pre_sum2.reverse()
        for i in range(len(pre_sum)):
            if pre_sum[i] ==pre_sum2[i]:
                return i
            
        return -1
        
            