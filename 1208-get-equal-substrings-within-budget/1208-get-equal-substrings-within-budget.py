class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        final = 0
        pref = [0]
        
        for i in range(len(s)):
            pref.append(pref[-1] + abs(ord(s[i]) - ord(t[i])))
       
        qu = deque()
        for j in range(len(pref)):
            while qu and  pref[j] - qu[0] > maxCost:
                qu.popleft()
            final = max(final, len(qu) )
            
            qu.append(pref[j])
        return final