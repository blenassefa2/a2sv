class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        """ 
                #declare variables

                # keep monotonicity

                # check condition 

            # max is decreasing
            # min is increasing
        """
        
        maxs, mins = deque(), deque()
        
        length = 1
        left = 0
        for i, val in enumerate(nums):
            
            while mins and nums[mins[-1]]  < val:
                mins.pop()
                
            while maxs and nums[maxs[-1]]  > val:
                maxs.pop()
            
            
            mins.append(i)
            maxs.append(i)
            
            while left <= i and maxs and mins and abs(nums[maxs[0]] - nums[mins[0]]) > limit:
                if maxs[0] == left:
                    maxs.popleft()
                if mins[0] == left:
                    mins.popleft()
                left += 1
            if mins and maxs:
                length = max(length, i - left + 1)
        return (length)