class Solution:
    def minInsertions(self, s: str) -> int:
        """
        my thought is to use stack to controll the balancedness of the parenthesis
        
        while building the stack
            -- when ever I reach '))' or ')' that does not have '(' pair I only add 1 to my number of tobe inserted count 
            -- when ever '(' finds its '))' pair with out need of any insertion it is poped from my stack
            
        
        after my stack is built it will contain either '(' or '()' that need either '))' or ')' respectively 
        thus each time I pop from my stack I add '2' or '1' depending on wehther I need '))' or ')' respectively
        
        """
        
        stack = []
        count = 0
        for i in range(len(s)):
            if s[i] == '(':
                if stack and stack[-1] == ")":
                    count += 1
                    stack.pop()
                    stack.pop()
                stack.append(s[i])
                
                continue
            if not stack:
                count += 1
                stack.append('(')
                stack.append(s[i])
            else:
                if stack[-1] == "(":
                    stack.append(s[i])
                else:
                    stack.pop()
                    stack.pop()
        while stack:
            if stack[-1] == ")":
                count += 1
                stack.pop()
                stack.pop()
            else:
                count += 2
                stack.pop()
        return count
            