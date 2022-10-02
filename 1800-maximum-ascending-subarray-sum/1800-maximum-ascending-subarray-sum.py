class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        """
        create the prefix sum of the numbers:
        
        create a window that is going to contain ascending numbers at index i
        if at certain index i, the nums[i] makes the window non-ascending when being added 
        
        the sum of the window will be recorded relative to the current max sum
        then new window with with only nums[i] will procede to run
        
        Time complexity = O(n)
        space complexit = O(1)
        """
        
        
        if len(nums) == 1:
            return nums[0]
        
        l,r = 0,1
        ls,le = 0, nums[0]
        final = 0
        while r < len(nums):
            
            if nums[r-1] < nums[r]:
                le += nums[r]
                r += 1
                final = max(final,le - ls)
                
            else:
                final = max(final,le - ls)
                ls = le
                le += nums[r]
                r += 1
                
            final = max(final,le - ls)     
                
                
                
                
              
                
            
                
        return final
            
            