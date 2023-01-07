class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        """
        TC: O(nlogn)
        SC: O(n)
        """
        # initialize variables
        newArray = list(range(len(nums)))
        previous = [-1, 0]
        
        newArray.sort(key = lambda x: nums[x])
        
        # iterate through newArray and update nums array
        for i in range(len(newArray)):
            if previous[0] == nums[newArray[i]]:
                nums[newArray[i]] = previous[1]
            else:
                previous = [nums[newArray[i]], i]
                nums[newArray[i]] = i
                
                
        return nums