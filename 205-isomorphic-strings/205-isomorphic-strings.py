class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        store = {}
        matched = set()
        for i in range(len(s)):
         
              
            if s[i] not in store and t[i] not in matched:
                
                store[s[i]] = t[i]
                matched.add(t[i])
                
            else:
                
                if s[i] in store :
                    if store[s[i]] == t[i]:
                        continue
                    elif store[s[i]] != t[i]:
                        return False
                elif t[i] in matched:
                    return False
                
                
        return True