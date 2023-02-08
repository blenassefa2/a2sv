class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        edges = defaultdict(list)
        start = deque([])
        answer = []
        visited = set()
        
        for x,y in adjacentPairs:
            edges[x].append(y)
            edges[y].append(x)
            
        
        for node in edges:
            if len(edges[node]) == 1: 
                start.append(node)
                
                break
        
        while start:
            
            node = start.popleft()
            
            answer.append(node)
            visited.add(node)
            for neighbor in edges[node]:
                if neighbor not in visited:
                    start.append(neighbor)
                    break
            
        return answer      
        