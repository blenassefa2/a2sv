class Solution:
    def sortSentence(self, s: str) -> str:
        new_s = s.split(" ")
        
        new_s.sort(key = lambda x: int(x[-1]))
        
        for i in range(len(new_s)):
            new_s[i] = new_s[i][:-1]
            
        
        return " ".join(new_s)