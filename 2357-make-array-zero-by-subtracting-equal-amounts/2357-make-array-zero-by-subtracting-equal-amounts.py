class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        """
        for this question I need to access the minimum value
        and do the operation each time where a value > 0 exists in nums
        
        Time Complexity: O(nlogn)
        SpaceComplexity: O(1)
        """
        #initialize variables
        operations = 0
        lastMin = 0
        
        
        # sort the array
        nums.sort()
        
        # iterate through the array checking if there is operation needed
        for i in range(len(nums)):
            if nums[i] - lastMin != 0:
                lastMin += (nums[i] - lastMin)
                operations += 1
        
        return operations