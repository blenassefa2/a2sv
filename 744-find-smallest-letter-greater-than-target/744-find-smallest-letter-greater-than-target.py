class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l,r = 0, len(letters) - 1
        
        best = ""
        while l<=r:
            
            mid = (l+r)//2
            
            if letters[mid] <= target:
                l = mid + 1
            else:
                best = letters[mid]
                r = mid -1
        if letters[mid] <= target and l == len(letters):
                return letters[0]
        return  best
              
                