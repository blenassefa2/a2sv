class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        
        best = x
        while l <= r:
            mid = ((r-l)//2 )+ l
            
            if mid*mid > x:
                r = mid - 1
            else:
                l = mid + 1
                best = mid
        return best