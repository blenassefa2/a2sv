class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l,r = 1, num
        
        while l <= r:
            mid = (l+r)//2
            
            if mid*mid == num:
                return True
            if mid*mid < num:
                l = mid + 1
            elif mid*mid  > num:
                r = mid -1
        return False
            
        