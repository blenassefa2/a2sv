class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        evens = [x for x in nums if x%2 == 0]
        odds = [y for y in nums if y%2 != 0]
        j = 0
        for i in range(len(nums)):
            if i < len(evens):
                nums[i] = evens[i]
            else:
                nums[i] = odds[j]
                j += 1
        return (nums)