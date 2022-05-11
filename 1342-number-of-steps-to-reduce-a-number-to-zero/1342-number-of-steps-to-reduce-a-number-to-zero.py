class Solution:
    def numberOfSteps(self, num: int) -> int:
        n = bin(num)
        n = n[2:]
        return n.count("0") + (n.count("1") *2) - 1