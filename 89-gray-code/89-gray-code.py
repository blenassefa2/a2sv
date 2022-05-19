class Solution:
    def grayCode(self, n: int) -> List[int]:
        ls = [0,1]
            
        mask = 3
        
        found = False
        while len(ls) < pow(2,n):
            a = []
            for i in ls:
                a.append(mask^i)
                if len(ls) + len(a) == pow(2,n):
                    found = True
                    break
            ls.extend(a)
            if found:
                break
            mask = mask << 1
        return ls