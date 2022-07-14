class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        Thought process:
        ----------------
        
        Since there is supposed to be every number from 1 we try to sort numbers inplace 
        starting from 1 by placing the numbers to their respective index
        if the number in a wrong position is > len(nums) or <= 0 then we let it be 
        if the wrong number is a duplicate and if its duplicate has already taken the index then let it be
        then what we do is find the first number that does not match to its index
        Complexity:
        -----------
        
        Time complexity O(Kn) = O(n)  # we touch each index maximum some constant times not n times
        space complexity O(33) = O(1)
        """
        x = max(nums)
        if x <= 0:
            return 1
        i = 0
        while i < len(nums):
            
            if nums[i] <= 0 or nums[i] > len(nums) or nums[i] == i + 1 or nums[i] == nums[nums[i] - 1]:
                i += 1
                continue
            
            
            j = nums[i] - 1
            
            nums[j], nums[i] = nums[i], nums[j] 
            
            
        for x in range(len(nums)):
            if nums[x] != x + 1:
                return x + 1
        
        return nums[-1] + 1
            
        
        
        
        