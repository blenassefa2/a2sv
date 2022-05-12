class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        a = 0
        for i in range(1,len(nums) + 1):
            a ^= i
        for j in range(len(nums)):
            a ^= nums[j]
        return a