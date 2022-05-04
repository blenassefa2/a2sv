class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        ans = [True]* len(queries)
        for i in range(len(queries)):
            p = 0
            q = 0
            while p < len(pattern):
                while q < len(queries[i]) and queries[i][q] != pattern[p]:
                    if ord(queries[i][q]) < 97:
                        
                        ans[i] = False
                        break
                    q +=1
                if p < len(pattern) and q == len(queries[i]):
                    ans[i] = False
                if not ans[i]:
                    break
                p += 1
                q+= 1
            if ans[i] == True:
                while q <len(queries[i]):
                    if ord(queries[i][q]) < 97:
                        
                        ans[i] = False
                        break
                    q += 1
                
        return ans
            