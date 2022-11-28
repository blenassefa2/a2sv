class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        
        count = defaultdict(int)
        right = 0
        left = 0
        while right < len(s):
            
            while right < len(s) and count[s[right]] < 1:
                count[s[right]] += 1
                maxLength = max(maxLength, right - left + 1)
                right += 1
                
            while right < len(s) and count[s[right]] >= 1:
                count[s[left]] -= 1
                left += 1
            maxLength = max(maxLength, right - left)
        return maxLength