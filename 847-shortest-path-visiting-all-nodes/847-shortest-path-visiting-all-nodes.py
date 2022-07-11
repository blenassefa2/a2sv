class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        """
        since normal bfs will not work because of repeated visites
        we need to change our way of keeping visited nodes
        
        here our visited nodes are represented as combination of 
        a node and the path it took to get there(represented as string of bits
        where a node traverersed is represented by one and not traversed by 0)
        
        """
        
        
        def bfs(node):
            visited = set()
            final = int("1"*len(graph),2)
            
            qu = deque([[(node, 1<<node ),0]])
            counts = 0
            while qu:
                x, count = qu.popleft()
                node, comb = x
                
                if comb == final:
                    return count
                if x in visited:
                    continue
                
                visited.add(x)
                
                for i in graph[node]:
                    tmp = 1<<i
                
                    qu.append([(i,tmp|comb),count + 1])
               
               
            return counts
        
        ans = 100000000
        for i in range(len(graph)):
            ans = min(ans, bfs(i))
        return ans