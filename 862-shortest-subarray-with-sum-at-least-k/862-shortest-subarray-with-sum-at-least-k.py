class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        pre = [0]
        
        for i in nums:
            pre.append(pre[-1] + i)
            
        final = len(nums) +1
        i = 0
        qu = deque([])
        while i < len(pre):
            
            
            while qu and pre[i] <=pre[qu[-1]]:
                qu.pop()
            
            while qu and pre[i] - pre[qu[0]] >= k:
                final = min(final, i - qu[0])
                qu.popleft()
            
            qu.append(i)
            i += 1
            
        return final if final <= len(nums) else -1