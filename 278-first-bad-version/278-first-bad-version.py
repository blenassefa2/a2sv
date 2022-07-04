# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        best = -1
        while left <= right:
            median = int(left + (right - left)/ 2)
            if isBadVersion(median) == False:
                left = median + 1
            else:
                best = median
                right = median - 1
        return best
        