
class Solution:
    def rob(self, nums: List[int]) -> int:
        @lru_cache(None)
        def rec(index,sum_):
            if index >= len(nums):
                return sum_
            sum_ += nums[index]
            return max(rec(index+2,sum_), rec(index+3,sum_))
        final =  -1
        for i in range(len(nums)):
            final = max(final, rec(i,0))
        return final