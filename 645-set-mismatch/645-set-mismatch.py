class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        repeated, affected = 0, 0
        s = list(set(nums))
         
        for x in range(len(nums)):
            positive = abs(nums[x])
            nums[positive - 1] *= -1
            if nums[positive -1] > 0:
                repeated = positive
            
            affected ^= ((x + 1) ^positive)
            
        
        return [repeated,affected^repeated] 
            