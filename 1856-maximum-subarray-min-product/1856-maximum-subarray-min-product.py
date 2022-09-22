class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        pre = [0]
        for i in nums:
            pre.append(pre[-1] + i)
       
        nums.append(-1)
        stack = []
        final = 0
        i = 0
        while i < len(nums):
           
            to_append = i
            while stack and stack[-1][0] > nums[i]:
                s, m = pre[i] - pre[stack[-1][1]], stack[-1][0]
                to_append = stack[-1][1]
                final = max(final, s*m)
                stack.pop()
            
        
            
            stack.append([nums[i], to_append])
            i += 1
        
        return final% 1000000007