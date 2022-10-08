class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        I am thinking of using stack + sliding window
        so that I can keep the length of the valid parentheses substring
        
        
        while building my stack there are three scenarios:
            1, I will pop valid parentheses
                increase curr_count by two
                procede as you normally would
            2, I will get an element that for sure makes the stack sofar invalid
                I update final_count if final_count < curr_count
                clean up the the stack and procede
            3, I will get an element whose outcome can not be determined yet
                append it to the stack as you normally would
        
        """
    
        stack = []
        curr = 0
        final = 0
        for i in range(len(s)):
            
            if s[i] == "(":
                stack.append([s[i],i])
            else:
                if stack and stack[-1][0] == "(":
                    curr = (i - (stack.pop())[1] +1)
                    if stack and stack[-1][0] == "h":
                        curr += stack.pop()[1]
                    stack.append(["h", curr])
                    final = max(final, curr)
                    
                elif len(stack) > 1 and stack[-1][0] == "h":
                    d = stack.pop()
                    c = stack.pop()
                    curr = i - c[1] + 1
                    if stack and stack[-1][0] == "h":
                        curr += stack.pop()[1]
                    final = max(final, curr)
                    stack.append(["h",curr])
                    
                else:
                    stack = []
                    curr = 0
           
        
                
        return final