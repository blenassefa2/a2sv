class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        
        while n > 0:
            count += n&1
            n//= 2
        return(count)