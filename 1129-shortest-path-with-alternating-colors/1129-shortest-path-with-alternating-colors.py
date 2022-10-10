class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        ans = [-1]*n
        
        edges = defaultdict(list)
        for l,r in redEdges:
            edges[l].append([r,'R'])
        
        for l,r in blueEdges:
            edges[l].append([r, 'L'])
            
        qu = deque([[0, '']])
        visited = set()
        level = 0
        while qu:
            N = len(qu)
            for i in range(N):
                node, color = qu.popleft()
                visited.add((node,color))
                if ans[node] == -1 :  ans[node] = level
                
                for n,c in edges[node]:
                    if c != color and (n,c) not in visited:
                        qu.append([n,c])
                
            level += 1
        
        return ans