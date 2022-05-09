class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = defaultdict(list)
        
        n["2"] =["a", "b","c"]
        n["3"] =["d", "e", "f"]
        n["4"] =["g", "h","i"]
        n["5"] =["j", "k", "l"]
        n["6"] =["m","n","o"]
        n["7"] =["p","q","r","s"]
        n["8"] =["t", "u", "v"]
        n["9"] =["w","x","y","z"]
        a = len(digits)
        if a == 0:
            return []
        if a == 1:
            return n[digits[0]]
        if a == 2:
            return [x+b for x, b in product(n[digits[0]], n[digits[1]])]
        if a == 3:
            return [x+b+c  for x, b, c in product(n[digits[0]], n[digits[1]],n[digits[2]])]
        return [x+b+c+d for x, b,c,d in product(n[digits[0]], n[digits[1]],n[digits[2]],n[digits[3]])]