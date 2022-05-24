class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        s= "".join(sorted(list(s)))
        init = (s.find(letter))
        count = 0
        while init < len(s) and s[init]  == letter:
            count +=1
            init += 1
        return int((count/len(s)) *100)