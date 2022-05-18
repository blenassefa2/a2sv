class Solution:
    def addBinary(self, a: str, b: str) -> str:
        y, x = int(a,2), int(b,2)
        sum_ = 0
        carry = 1
        while carry:
            sum_, carry = (x^y), ((x&y) <<1)
            x,y = sum_,carry
        return bin(sum_)[2:]