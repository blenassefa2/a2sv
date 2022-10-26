class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        qu = deque([])
        i = 0
        ans = []
        for j in range(len(nums)):
            while qu and nums[qu[-1]] <= nums[j]:
                qu.pop()
                
            qu.append(j)
           
            
                
            if j - i+1 ==k:
                ans.append(nums[qu[0]])
                i += 1
                if i > qu[0]:
                    qu.popleft()
        return ans
        