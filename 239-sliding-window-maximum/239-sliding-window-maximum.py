class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        when the window is sliding we need to keep track of the potential maximums
        
        if our current potential is not in the window
            it needs to be removed
        if the coming value is greater than our recent potential:
            our recent potential is not needed anymore
        
        after everything is adjusted the current potential is recorded
        
        """
        
        qu = deque()
        l,r = 0,0
        ans = []
        for i in range(len(nums)):
            
            
            if qu and qu[0] < l:
                qu.popleft()           
            while qu and nums[i] > nums[qu[-1]]:
                qu.pop()
          
            r += 1
            qu.append(i)
            if r -l == k:
                l += 1
                ans.append(nums[qu[0]])
            
            
        return ans