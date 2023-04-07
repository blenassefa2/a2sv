class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        best = []
        for i in nums:
            if not best:
                best.append(i)
            else:
                if best[-1] != i:
                    best.append(i)
                    
        if best[-1] == best[0] and len(best) > 1:
            best =best[:-1]
            
        left = 0
        right = len(best) - 1
        while left < right:
            mid = (left + right)//2
            
            if best[mid] > best[right] :
                left = mid + 1
            
            else:
                
                right = mid
     
        return best[right]