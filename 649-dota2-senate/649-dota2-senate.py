class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r,d = deque(), deque()
        
        for i in range(len(senate)):
            if senate[i] == "R":
                r.append(i)
            else:
                d.append(i)
        n = len(senate) 
        while r and d:
            
            R, D = r.popleft(), d.popleft()
            
            if R < D:
                r.append(n + R)
            else:
                d.append(n + D)
        
            
        
        return "Radiant" if r else "Dire"
            
            
            
            
            