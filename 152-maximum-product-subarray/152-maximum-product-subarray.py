class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            if nums[i-1] == 0:
                continue
            nums[i] = nums[i] * nums[i -1]
            
        final = -1000000000000000000000000000
        first_neg = 0

        for i in range(len(nums)):
            if nums[i] >= 0:
                if nums[i] == 0:
                    first_neg = 0
                final = max(final, nums[i])
            else:
                if not first_neg:
                    first_neg = nums[i]
                    final = max(final, nums[i])
                else:
                    final = max(final, nums[i]//first_neg)
        
        return final
         