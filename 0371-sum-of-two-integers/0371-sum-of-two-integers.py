class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        max_int = 0x7D0
        mask = 0xfff
        def add(a,b):
            sum_, carry = 0,1
            
            while carry:
                sum_, carry = (a^b)& mask, ((a&b) <<1)& mask
                a,b = sum_, carry
            return sum_
          
       
        
        ans = add(a,b)
       
        return (~(ans^mask))  if ans > max_int else ans