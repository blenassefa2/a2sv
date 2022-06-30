class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word = 0
        s= list(s)
     
        p = len(s) -1
        while p >= 0 and s[p] == ' ':
            p -= 1
        while p >= 0 and s[p] != ' ':
            p -= 1
            word += 1
        
            
        return(word)
        