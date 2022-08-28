class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        
        gas = [1,2,3,4,5], cost =
             -[3,4,5,1,2]
              [-2, -2 , -2, 3, 3] 
                     
              [5,8,2,8]
              [6,5,6,6]
               -1 3 -4 2
              [2,3,4], 
              [3,4,3]
              
              -1 -1 1
        
        checker start: true if dest == start else false
        
        
        
        """
        
        stuff = [gas[i] - cost[i] for i in range(len(gas))]
        
        if sum(stuff) < 0:
            return -1
        stack = []
        i = 0
        while len(stack) < len(stuff):
            i  %= len(stuff)
            if not stack:
                if stuff[i] >= 0:
                    stack.append([stuff[i], i])
                i += 1
                continue
            if stack[-1][0] + stuff[i] >= 0:
                stack.append([stuff[i] + stack[-1][0], i])
            else:
            
                stack = []
            i += 1
        return stack[0][1]