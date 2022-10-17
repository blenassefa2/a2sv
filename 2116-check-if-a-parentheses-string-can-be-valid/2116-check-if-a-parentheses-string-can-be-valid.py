class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        unlocked = []
        open_locked = []
        
    
        for i,v in enumerate(s):
            if locked[i] == "1":
                if v == ")":
                    if not open_locked  and not unlocked:
                        return False
                    if open_locked:
                        open_locked.pop()
                    else:
                        unlocked.pop()
                else:
                    
                    open_locked.append(i)
            else: 
                unlocked.append(i)
           
       
        while open_locked and unlocked:
            if unlocked[-1] < open_locked[-1]:
                return False
            unlocked.pop()
            open_locked.pop()
            

         
        return  len(unlocked) %2 == 0 and not open_locked