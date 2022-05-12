class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        ls= [0,1]
         
            
        while len(ls) <= n:
            t = []
            for l in ls:
                t.append(l+1)
                if len(t) + len(ls) > n:
                    break
            ls.extend(t)
        return(ls)
            
        
        
            
        