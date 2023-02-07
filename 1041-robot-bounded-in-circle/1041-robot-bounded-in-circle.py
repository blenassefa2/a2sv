class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        """
        One thought that cross my mind is
        
        as long as we have G it will go straight
        
        but if we have L or R then it will make turns eventually creating circle
        
        if we have L and R together then they will cancel out eachother and restoring the only G situation
        
        so we can use stack to check if L and R will cancel out eachother
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        """
        # initialize variables
        stack = []
        i = 0
        gCount = 1
        
        # loop through instructions canceling out L and Rs
        while i < len(instructions):
            
            if instructions[i] != 'G':
                if not stack or instructions[stack[-1]] == instructions[i]:
                    stack.append(i)
                    
                else:
                    
                    stack.pop()
            else:
                gCount += 1
                   
            i += 1
        
        if not stack:
            if "G" in instructions:
                return False
            return True
        
      
        
        gos = 0
        d = 1
        change = 0
        instructions = instructions *4
        for i in range(len(instructions)):
            
            if instructions[i] == 'G':
                gos += d
            elif i%(len(instructions)// 4) in stack:
                change += 1
                change %= 4
                if change == 0 or change == 1:
                    d = 1
                else:
                    d = -1
                
        return gos == 0
                