class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        mid = len(strs)//2
        left = self.longestCommonPrefix(strs[0:mid])
        right = self.longestCommonPrefix(strs[mid:len(strs)])
        
        ans, i = "", 0
        
        while i < len(left) and i < len(right):
            if left[i] == right[i]:
                ans += left[i]
            else:
                break
            i += 1
        return ans
            