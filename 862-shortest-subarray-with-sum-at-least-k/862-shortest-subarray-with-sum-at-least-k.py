class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        """
        1. have prefix array
        2. do a sliding window on the prefix array
        
        """
        pre = [0]
        mnlen = len(nums) + 1
        qu = deque()
        
        for i in nums:
            pre.append(pre[-1] + i)
            
        for i, n in enumerate(pre):
            
            # to make sure the qu is monotonically increasing
            while qu and pre[qu[-1]] >= n:
                qu.pop()
                
            # if we achieve our target we try to reduce window size
            # to see if we can get shorter sub array
            while qu and n - pre[qu[0]] >= k:
                mnlen = min(mnlen, i - qu.popleft())
            
            qu.append(i)
        
        return -1 if mnlen == len(nums) + 1 else mnlen