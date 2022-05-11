class Solution:
    def numberOfSteps(self, num: int) -> int:
         
        return ((bin(num))[2:]).count("0") + (bin(num)[2:].count("1") *2) - 1