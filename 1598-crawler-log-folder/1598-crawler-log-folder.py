class Solution:
    def minOperations(self, logs: List[str]) -> int:
        """
        for this question I am thinking of keeping a stack
        
        so when ever there is 
        ../ operation we pop from the stack
        ./  operation nothing occures
        other operation pushes on to the stack
        
        the length of the stack will be number of steps for going back
        
        Time complexity: O(n)
        space complexity: O(n)
        
        """
        # initialize variables
        stack = []
        
        # simulate the logs to end up with opened folders
        for operation in logs:
            
            if operation != './':
                if operation == '../':
                    if stack:
                        stack.pop()
                else:
                    stack.append(operation)

        return len(stack)