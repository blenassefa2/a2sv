class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) >= len(t):
            return s==t
        # if not(s;)
        i = 0
        stack = ""
        
        for j in range(len(t)):
            if i < len(s) and  s[i] == t[j]:
                stack += t[j]
                i+= 1
        return stack == s