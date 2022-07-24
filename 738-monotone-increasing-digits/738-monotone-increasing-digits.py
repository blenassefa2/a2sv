class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        """
        n = 12432
        12399
        
        I am changing the numbers so they are monotically increasing
        and also keeping track of the recently updated index/digit
        
        at the end all digits after the last converted will be 9
        
        
        999999
         
        159935678
                |
        
        """
        s = list(str(n))
        
        last = len(s) + 3
        
        for i in range(len(s) - 1, 0, -1):
            if s[i] < s[i-1]:
                last = i
                s[i - 1] = str(int(s[i-1]) - 1)
                
        if  last == len(s) + 3:
            return n
        
        for i in range(last, len(s)):
            s[i] = "9"
            
        return int("".join(s))
        
        
        
        