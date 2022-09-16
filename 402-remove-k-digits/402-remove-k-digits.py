class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        i = 0
        while i < (len(num)):
            if not stack:
                stack.append(num[i])
                i += 1
                continue
            
            if num[i] < stack[-1] and k > 0:
                stack.pop()
                k -= 1
                continue
            stack.append(num[i])
            i += 1
        
                
        
        
        stack = stack[:-1*k] if k>0 else stack
        
        return "0" if not stack else str(int("".join(stack)))
            