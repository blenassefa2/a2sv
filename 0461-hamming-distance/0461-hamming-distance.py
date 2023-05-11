class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        temp = x^y
        
        difference = 0
       
        for i in range(31):
            
            difference += ((temp &(1<<i)) != 0)
            
            
        return difference