class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        self.ans = []
        
        n = defaultdict(list)
        
        n["2"] =["a", "b","c"]
        n["3"] =["d", "e", "f"]
        n["4"] =["g", "h","i"]
        n["5"] =["j", "k", "l"]
        n["6"] =["m","n","o"]
        n["7"] =["p","q","r","s"]
        n["8"] =["t", "u", "v"]
        n["9"] =["w","x","y","z"]
        
        
        def recurs(index, combo):
            if index >= len(digits):
                if combo:
                    self.ans.append(combo)
                return
            
            for i in n[digits[index]]:
                recurs(index + 1, combo + i)
        recurs(0,"")       
        return self.ans