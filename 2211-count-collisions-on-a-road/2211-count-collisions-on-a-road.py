class Solution:
    def countCollisions(self, directions: str) -> int:
        i = 0
        cars = list(directions)
        old_state = list(directions)
        stack = []
        
        okay = lambda a,b: a == b or a == "L" or (a =="S" and b == "R")
        
        
        while i < len(cars):
            if not stack:
                stack.append(cars[i])
                i += 1
                continue
                
            if okay(stack[-1], cars[i]):
                stack.append(cars[i])
                i += 1
                continue
            
            popped = stack.pop()
            if popped == "S":
                stack.extend(['S', 'S'])
                i += 1
            else:
                cars[i] = "S"
                cars[i - 1] = "S"
                i -= 1
        
        
        collisions = 0
        for j in range(len(cars)):
            if old_state[j] != stack[j]:
                collisions += 1
        return collisions
        
        