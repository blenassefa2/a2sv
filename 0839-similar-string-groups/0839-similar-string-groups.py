class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        roots = [0]
        strs = list(set(strs))
        roots = [x for x in range(len(strs))]
        similar = defaultdict(bool)
        def similarity(s1, s2):
            diff = 0
            for y in range(len(s1)):
                if s1[y] != s2[y]:
                    diff += 1
            return diff <= 2
        for i in range(len(strs)):
            for j in range(i,len(strs)):
                similar[(strs[j], strs[i])] = similarity(strs[j], strs[i])
        
        def root(a):
            
            while a != roots[a]:
                roots[a] = roots[roots[a]]
                a = roots[a]
            return a
        
        def union(a, b):
            roota = root(a)
            rootb = root(b)
            if roota != rootb:
                    
                for i in range(len(roots)):
                    if roots[i] == roota and similar[(strs[i], strs[b])]:
                        roots[rootb] = roota
                        return
                    
                    if roots[i] == rootb and similar[(strs[i], strs[a])]:
                        roots[roota] = rootb                 
            
        """Driver code"""
        for i in range(len(strs)):
            for j in range(len(strs)): 
            
                union(i, j)
        return len(set(roots))