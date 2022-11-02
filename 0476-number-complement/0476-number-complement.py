class Solution:
    def findComplement(self, num: int) -> int:
        newNum = 0
        currentBit = 0
        while num:
            if num & 1 == 0:
                newNum += pow(2,currentBit)
            num >>= 1
            currentBit += 1
        return newNum