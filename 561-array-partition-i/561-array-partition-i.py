class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        for i in range(len(nums) -2, -1, -2):
            ans += nums[i] 
        return ans