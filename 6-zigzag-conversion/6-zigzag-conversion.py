class Solution:
    def convert(self, s: str, numRows: int) -> str:
       
        i = 0
        lis = []
        while i < len(s) and i < numRows:
            lis.append(s[i])
            i += 1
        
        
        while i < len(s):
            flag = numRows - 2
            while flag > 0 and i < len(s):
                lis[flag] += s[i]
                flag -= 1
                i += 1
            
            flag = 0
            while flag < numRows and i < len(s):
                lis[flag] += s[i]
                flag += 1
                i += 1
        return "".join(lis)