class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
      

        nums.sort()
        ans = 0
        temp = []
        for i in nums:
            lower_i = bisect.bisect_left(temp,lower-i)
            upper_i = bisect.bisect_right(temp,upper-i)
            ans += upper_i - lower_i
            temp.append(i)
        return ans