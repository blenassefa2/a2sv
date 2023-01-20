class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            s = str(x)
        else:
            s = str(x)[1:]
        h = 1
        i = 0
        nw = 0
        while i < len(s):
            nw += h*(ord(s[i])- ord("0"))
            h *= 10
            i += 1
        if x <0:
            if nw* -1 < -2147483648:
                return 0
            return nw* -1
        if nw > 2147483647:
            return 0
        return nw