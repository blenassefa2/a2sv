class Solution:
    def calculate(self, s: str) -> int:
        """
        for this question I am going to use stack to calculate the equation
        
        
        when ever there is a negative sign I will multiply the number imediately 
        coming after the sign will be multiplied by -1 and pushed back
        
        if ')' sign is coming then all values on stack until a '(' sign will be popped and added
        then the sum will be pushed back to the stack
        
        in the end all of the elements remaining in the stack will be summed
        
        and that will be the result
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        """
        
        stack = []
       
        val, num, sign = 0, 0, 1

        for c in s:
            if c in '+-':
                val += sign * num
                sign = 1 if c == '+' else -1
                num = 0
            if c == '(':
                stack.append(val)
                val = 0
                stack.append(sign)
                sign = 1
            if c == ')':
                val += sign * num
                val *= stack.pop()
                val += stack.pop()
                num = 0
            if c.isdigit():
                num = num * 10 + int(c)
        return val + num * sign