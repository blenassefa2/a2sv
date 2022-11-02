class Solution:
    def findComplement(self, num: int) -> int:
      
        return num ^ ((1 << (floor(log2(num)) + 1))-1)