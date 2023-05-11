class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        max_int = 0x7D0
        mask = 0xfff
        
       
        ans, carry = 0,1

        while carry:
            ans, carry = (a^b)& mask, ((a&b) <<1)& mask
            a,b = ans, carry
            
          
       
        
     
       
        return (~(ans^mask))  if ans > max_int else ans