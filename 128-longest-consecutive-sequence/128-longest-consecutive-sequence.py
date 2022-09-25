class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        visited = set()
        
        final = 0
        curr = 0
        for i in nums:
            if i in visited:
                continue
            m,b = i, i +1
            curr = 0
            while m in s:
                visited.add(m)
                m -= 1
                curr += 1
            while b in s:
                visited.add(b)
                b += 1
                curr += 1
            final = max(final, curr)
        return final
                
                