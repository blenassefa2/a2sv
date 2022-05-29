class Solution:
    def maxProduct(self, words: List[str]) -> int:
        ans = 0
        mapp = defaultdict(set)
        for x in range(len(words)):
            for y in words[x]:
                mapp[x].add(y)
       
        for i in range(len(words)):
            for j in range(len(words)):
                u  = (mapp[i].union(mapp[j]))
               
                if (len(mapp[i]) + len(mapp[j])) == len(u):
                    ans = max(ans, len(words[i]) * len(words[j]))
        return(ans)
                
            
                
        