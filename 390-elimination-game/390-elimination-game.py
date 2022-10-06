class Solution:
    def lastRemaining(self, n: int) -> int:
        """
        during each step i we have two end points a, b and some number of elements n for us to deal with.
        all we need to do is keep track of our starting pos, a,b,i, and n  and continue with the steps until a == b
        ans = 
        for each step i:
            if n is odd:
                    a += pow(2^step)
                    if a >= b:
                        return b
                    b -= pow(2^step)
                    if a >= b:
                        return a
                    
            else:
                if pos == 0:
                    a += pow(2^step)
                    if a >= b:
                    return b
                else:
                    b -= pow(2^step)
                    if a >= b:
                        return a
            step +=1
            n //=2
            pos = -1 if not pos else 0       
        Time complexity: O(log(n))
        Space complexity: O(1)
        
        """
        
        pos, a, b, n, step = 0, 1, n, n, 0
        while True:
            if n%2:
                a += pow(2,step)
                if a >= b:
                    return b
                b -= pow(2,step)
                if a >= b:
                    return a
                    
            else:
                if pos == 0:
                    a += pow(2,step)
                    if a >= b:
                        return b
                else:
                    b -= pow(2,step)
                    if a >= b:
                        return a
            step +=1
            n //=2
            pos = -1 if not pos else 0 
            