class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        start = 1 << k - 1
        end = (1 << k)
       
        for i in range(start,end):
            x =bin(i)[2:]
            
         
            if x not in s:
                return False
        if "0"*len(bin(end-1)[2:]) not in s:
            return False
        
        return True
        