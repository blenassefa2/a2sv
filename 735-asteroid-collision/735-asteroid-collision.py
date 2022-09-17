class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        i = 0
        while i < len(asteroids):
            if not stack:
                stack.append(asteroids[i])
                i+= 1
                continue
            
            if (asteroids[i]//abs(asteroids[i])) >= (stack[-1]//abs(stack[-1])):
                stack.append(asteroids[i])
            else:
                
                popped = stack.pop()
                if abs(popped) < abs(asteroids[i]):
                    continue
                if abs(popped) > abs(asteroids[i]):
                    stack.append(popped)
            i += 1
        return stack