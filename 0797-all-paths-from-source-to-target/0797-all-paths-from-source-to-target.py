class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        qu = deque([[0,[0]]])
        
        final = []
        while qu:
            N = len(qu)
            for _ in range(N):
                node, collect = qu.popleft()

                if node == len(graph) - 1:

                    final.append(collect)
                    continue
                    
                for i in graph[node]:
                    x = [j for j in collect]
                    x.append(i)
                    qu.append([i, x])
                
        return final