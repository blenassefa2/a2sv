class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [comb(rowIndex, i) for i in range(rowIndex + 1)]
        
        return ans