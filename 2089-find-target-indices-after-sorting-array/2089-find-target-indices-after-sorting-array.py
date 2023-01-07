class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        """ 
        To have TC of O(n) I will use count sort SC of O(1)
            *without counting the space used for output
            
            
            
            All we need is the 
                f = frequency of the target and 
                s = number of elements < target
                
            then the answer = [s, s+1, s+2,,,,s+f-1]
        """
        # initialize the needed variables
        length = 0
        less = 0
        
        # iterate throught nums and update the length and less
        for value in nums:
            if value < target:
                less += 1
            elif value == target:
                length += 1
                
        # return the answer
        return list(range(less,less + length))
        
        