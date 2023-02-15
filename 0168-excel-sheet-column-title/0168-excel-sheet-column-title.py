class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        col = []
       
        letters = 26
        while columnNumber > 0:
            columnNumber -= 1
            ind = columnNumber % letters
            col.append(chr(ord("A") + ind))
            columnNumber //= letters
            
        return "".join(col[::-1])