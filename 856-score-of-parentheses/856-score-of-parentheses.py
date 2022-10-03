class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        """
        we are going to use stack to keep track of the score
        
        we are alway going to have either '(' or ')' as our next index:
        if '('
            we append to our stack no matter what
        if ')'
            we pop from the stack
                if the poped value is a digit
                    we pop again and remove the '(' and double the digit
                else create digit = 1
                then
                if currently the top of the stack is a digit then pop as digit2
                    then push digit2 + 2digit
                else just push 2digit
              
                    
        return what is left in the stack
        
        Time complexity = O(n)
        Space complexity = O(n)
        """
        
        stack = ['(']
        for i in range(1,len(s)):
            
            if s[i] == '(':
                stack.append(s[i])
                continue
            digit = 1
            if stack[-1] != '(':
                digit = 2*stack.pop()
            stack.pop()
            if stack and stack[-1] != '(':
                digit += stack.pop()
            stack.append(digit)
        return stack[0]