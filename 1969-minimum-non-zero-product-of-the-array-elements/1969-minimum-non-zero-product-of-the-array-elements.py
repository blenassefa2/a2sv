class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        """
        [001, 010, 011, 
         100, 101, 110, 111]
        
        0001
        0010
        0011
        0100
        0101
        0110
        0111
        1000
        1001
        1011
        1100
        1101
        1110
        1111
      
        """
        _max = 2**p - 1
        MOD = (10**9) + 7
        return  (pow(_max - 1, ((_max + 1)// 2) -1 , MOD)  * _max)  % MOD
        