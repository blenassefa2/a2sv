class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1, stack2 = [], []
        
        for i in range(len(s)):
            if stack1 and s[i] == "#":
                stack1.pop()
            elif s[i] != "#":
                stack1.append(s[i])
        for j in range(len(t)):
            if stack2 and t[j] == "#":
                stack2.pop()
            elif t[j] != "#":
                stack2.append(t[j])
        return ("".join(stack1)) == ("".join(stack2))
                