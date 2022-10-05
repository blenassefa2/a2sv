class Solution:
    def isHappy(self, n: int) -> bool:
        
        nprev = {n}
        while n != 1:
            b = n
            n = 0
            while b:
                n += ((b%10)*(b%10))
                b //= 10
           
            if n in nprev:
                return False
            nprev.add(n)
        return True