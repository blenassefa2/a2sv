class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        line = [0]*(len(s)+1)
        s = list(s)
        for b,e,d in shifts:
            line[b] += 1 if d else -1
            line[e +1] -= 1 if d else -1
        for i in range(1, len(line)):
            line[i] += line[i -1]
        
        for i in range(len(line)):
            line[i] = (line[i]% 26)
     
        for i in range(len(s)):
            temp = (ord(s[i]) +line[i])
            if temp < 97:
                temp = 26+ temp
            elif temp > 122:
                temp = temp -26
    
            s[i] = chr(temp)
         
       
        return "".join(s)
        
        