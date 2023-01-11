class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        """
        Approach: I am going to use heap track of the biggest number I can add on my score
        Algorithm:
        store in maxheap
        while k > 0
            pop from heap
            update score
            update and push the popped value
            update k
        return value
        
        Time complexity klog(n)
        space complexity = O(1)
        
        """
        # initialize variables
        score = 0
        
        # organize in max heap
        for i in range(len(nums)):
            nums[i] *= -1
            
        heapify(nums)
        
        # loop until k decreases to 0 updating your score
        while k > 0:
            val = heappop(nums)
            score += -val
            heappush(nums, -ceil(-val/3))
            k -=1
            
        return score
    