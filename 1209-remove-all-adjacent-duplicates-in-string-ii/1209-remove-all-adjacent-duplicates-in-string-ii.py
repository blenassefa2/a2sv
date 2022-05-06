class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        i,c = 0,0
        
        stack = []
        
        while i < len(s):
            if not stack:
                stack.append(s[i])
                c += 1
                i+= 1
                continue
            if s[i] == stack[-1]:
                c += 1
                if c == k:
                    for a in range(k-1):
                        stack.pop()
                    c = 0
                    t = len(stack) - 1
                    
                    while t >= 0  and stack[t] == stack[-1]:
                        c +=1
                        t -= 1
                        
                        
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])
                c = 1
            i+=1
        
        return "".join(stack)
            