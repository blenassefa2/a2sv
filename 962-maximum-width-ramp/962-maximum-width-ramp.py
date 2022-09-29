class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        """
        if we have a monotonically decreasing stack 
            we can make sure that we are keeping the smallest i's therefore max width
            what ever comes in the future will have one of the i's in the stack as their left side
        
        if we are on a new index and that index makes our stack non decreasing:
            we calculate the ramp widith with it being the right side for all potential i's in the stack
            we also keep track of maximum width
            
        we return the stored maximum width
        
        time complexity: -  O(n)
        space complexity: - O(n)
        """
        
        
        stack = []
        final = 0
        
        for i in range(len(nums)):
            if not stack:
                stack.append(i)
                continue
            
            if nums[stack[-1]] <= nums[i]:
                x = len(stack) -1 
             
                while x >= 0 and nums[stack[x]] <= nums[i]:
                    
                    final = max(final, i - stack[x])
                    
                    x -= 1
            else:
                stack.append(i)
        return final