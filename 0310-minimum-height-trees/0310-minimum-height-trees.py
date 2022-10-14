class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
    
        if n <= 2:
            return [i for i in range(n)]
        
        indegree = defaultdict(int)
        e = defaultdict(list)
        for i,j in edges:
            indegree[i] += 1
            indegree[j] += 1
            e[i].append(j)
            e[j].append(i)
        qu = deque()
        for i in indegree:
            if indegree[i] ==  1:
                qu.append(i)
        
        final = []
        level = 0
        while qu:
            
            N = len(qu)
            for _ in range(N):
                node = qu.popleft()
             
                indegree.pop(node)
                final.append([node,level])
                             
            
                while e[node]:
                    i = e[node].pop()
                    indegree[i] -= 1
                    if indegree[i] == 1:
                        qu.append(i)
            level += 1
        ans =[]
        while final and final[-1][1] == level-1:
            
            ans.append(final.pop()[0])
            
        return ans
            
        
        
            
        
        
        
        
        
            