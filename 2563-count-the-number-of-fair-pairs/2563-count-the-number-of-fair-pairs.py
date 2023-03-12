class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
      

        nums.sort()
        ans = 0
        for i in range(len(nums)):
            lower_i = bisect.bisect_left(nums,lower-nums[i],hi=i)
            upper_i = bisect.bisect_right(nums,upper-nums[i],hi=i)
            ans += upper_i - lower_i
        return ans