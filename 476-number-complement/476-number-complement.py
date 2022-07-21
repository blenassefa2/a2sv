class Solution:
    def findComplement(self, num: int) -> int:
        size = floor(log2(num)) + 1
        ones_ = (1<<size) - 1
        return ones_ ^ num