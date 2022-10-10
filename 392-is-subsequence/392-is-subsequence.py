class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        hsh = defaultdict(list)
        
        for i in range(len(t)):
            hsh[t[i]].append(i)
            
        small = -1
        
        for a in s:
            if a in hsh:
                x = 0
                while x < len(hsh[a]) and hsh[a][x] <= small:
                    x += 1
                else:
                    if x >= len(hsh[a]) or hsh[a][x] <= small:
                        return False
                    
                    small = hsh[a][x]
            else:
                return False
        return True