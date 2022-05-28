class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s = ["".join(sorted(list(a))) for a in strs]
        
        di = defaultdict(list)
        
        for i in range(len(s)):
            di[s[i]].append(i)
            
        ans = []
        
        for x in di:
            temp = []
            for b in di[x]:
                temp.append(strs[b])
            ans.append(temp)
        return ans