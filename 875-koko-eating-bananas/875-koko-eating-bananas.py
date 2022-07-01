class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def magic(n):
            ans = 0
            for i in piles:
                ans += ceil(i/n)
                
            return ans
        
        l, r  = 1, max(piles)
        best = r
        while l <= r:
            mid = (l + r)//2
            
            if magic(mid) > h:
                l = mid + 1
            else:
                r = mid - 1
                best = mid
        return best