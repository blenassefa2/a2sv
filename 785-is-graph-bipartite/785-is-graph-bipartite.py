class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        m = len(graph)
        color = [-1]*m
        color[0] = 1
        
        
        
        visited = set()
        def bfs(w):
            qu = deque([w])
            color[w] = 1
            while qu:
                n = qu.popleft()
                visited.add(n)
                for i in graph[n]:
                    if i not in visited:
                        x = (color[n] -1)* - 1
                        if color[i] == -1:
                            color[i] = x
                            qu.append(i)
                        elif color[i] == x:
                            qu.append(i)
                        elif color[i] != x:
                            return False
                
            return True
    
        """Driver code"""
        ans = True
        
        for y in range(m):
            if y not in visited:
                if not bfs(y):
                    return False
        print(color)
        return ans
                    