class Solution:
    def countSubstrings(self, s: str) -> int:
        def ispali(a,b):
            count  = 0
            
            while a >= 0 and b < len(s) and s[a] == s[b]:
                a -=1
                b += 1
                count += 1
            return count
            
        ans = 0
        for i in range(len(s)):
            ans += ispali(i,i) + ispali(i,i+1)
        return ans