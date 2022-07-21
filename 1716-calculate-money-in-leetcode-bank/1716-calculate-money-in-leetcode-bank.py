class Solution:
    def totalMoney(self, n: int) -> int:
        full_weeks = n // 7
        total = 0
        if full_weeks:
            total = int((full_weeks/2)*(56 + ((full_weeks - 1)*7)))
    
        i = full_weeks +1
        while  n % 7:
            total += i
            n -= 1
            i += 1
        return total  
        """
        23//7 = 3
        
        total = 21+ 28 = 49
        
        """