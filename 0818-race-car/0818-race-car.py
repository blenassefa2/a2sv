class Solution:
    def racecar(self, target: int) -> int:
        """
        I think I can use bfs for this
        """
        
        qu = deque([(0, 1, 0)])
        visited = set()        
        
        while qu:
            
            currPos, currSpeed, level = qu.popleft()
            
            if currPos == target:
                return level
            
            if (currPos, currSpeed) in visited:
                continue
                
            visited.add((currPos, currSpeed))
            # If I choose A
            qu.append((currPos + currSpeed, currSpeed*2, level + 1))
            
            # if I choose B
            if currSpeed > 0:
                qu.append((currPos, -1, level + 1))
            else:
                qu.append((currPos, 1, level + 1))
        
                