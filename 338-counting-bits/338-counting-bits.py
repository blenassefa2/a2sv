class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        ls= [0,1]
        
        x = 0 
        for i in range(2, n+1):
            if not i & i - 1:
                x += 1
            
            a = (i -(1 << x))
            ls.append(ls[a] +1)
   
                
        return(ls)
            
        
        
            
        