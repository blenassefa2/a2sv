class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        winner = [None, 0]
        
        for i in range(len(nums)):
            if not winner[1]:
                winner[0] = nums[i]
                
            winner[1] += (1 if nums[i] == winner[0] else -1)
        return winner[0]
        