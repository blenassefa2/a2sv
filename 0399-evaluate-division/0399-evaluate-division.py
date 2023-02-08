class Solution:
    def bfs(self, node1, node2, edges):
        qu = deque([[node1, 1]])
        visited = set()
        while qu:
            node, value = qu.popleft()
            
            if node == node2:
                return value
            
            if node in visited:
                continue
            visited.add(node)
            
            for val, chain in edges[node]:
                qu.append([chain,val* value])
        return -1
                
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
        For this problem we can relate the variables with an edge value as their division value
        
        then substituting each query until we have the values we need
        
        """
        
        # initialize variables
        edges = defaultdict(list)
        answer = []
        
        # construct graph
        for i in range(len(equations)):
            a, b = equations[i]
            edges[a].append((values[i], b))
            edges[b].append((1/values[i], a))
        
        # Driver Code
        for a, b in queries:
            if a not in edges or b not in edges:
                answer.append(-1)
                continue
            ans = self.bfs(a,b, edges)
            if ans == -1:
                ans = self.bfs(b,a, edges)
            answer.append(ans)
        return answer