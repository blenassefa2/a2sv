class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s)  < k:
            return 0
        count = defaultdict(int)
        for i in s:
            count[i] += 1
        
        low, high, n_low = 0 , len(s) -1, 0
        
        for i in range(high + 1):
            if count[s[i]] < k:
                n_low = i
                return max(self.longestSubstring(s[0:n_low],k), self.longestSubstring(s[n_low+1:high + 1], k))
        if n_low == 0:
            return len(s)