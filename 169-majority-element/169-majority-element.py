class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) == 1:
            return nums[0]
        winner = [nums[0], 1]
        
        for i in range(1, len(nums)):
            if winner[0] == nums[i]:
                winner[1] += 1
                if winner[1] > floor(len(nums) /2):
                    return winner[0]
            else:
                winner = [nums[i], 1]
        