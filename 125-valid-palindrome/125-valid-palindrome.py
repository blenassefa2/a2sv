class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        
        s1,s2 = "",""
        stack = []
        
        for i in s:
            if i.isalnum():
                stack.append(i.upper())
        s1 = "".join(stack)
        for i in range(len(stack)):
            s2 += stack.pop()
            
        return s1 == s2