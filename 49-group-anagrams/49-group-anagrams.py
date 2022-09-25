class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s = defaultdict(list)
        
        for a in strs:
           
            s["".join(sorted(a))].append(a)
        
        return s.values()
                