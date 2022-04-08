class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        def dfs(root, visited, safe):
            if root  in visited:
                safe[root] = False
                return False
            if not graph[root]:
                safe[root] = True
                return True
            if root in safe:
                return safe[root]
            
            
            ans = True
            visited.add(root)
            for j in graph[root]:
                safe[j] = dfs(j,visited, safe)
                 
                ans = ans and safe[j]
            safe[root] = ans
            
            visited.remove(root)
            return ans
        
        """ driver code"""
        safe = defaultdict(bool)
        visited = set()
        for i in range(len(graph)):
            if i in safe:
                continue
            
            dfs(i, visited,safe)
            
     
        
        """ answer finalization """
        ans = []
        for x in safe:
            if safe[x]:
                ans.append(x)
        ans.sort()
        return ans