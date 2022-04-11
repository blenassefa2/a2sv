class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """ store connections"""
        n = len(isConnected)
        graph = []
        
        for i in range(n):
            for j in range(i,n):
                if isConnected[i][j] == 1:
            
                    graph.append([i,j])
            
       
        
        
        def dfs(root, safe):
            
            if  root in safe:
                return
            

            safe.add(root)
            for j in range(len(graph)):
                if graph[j][0] == root and graph[j][1] != root:
                    dfs(graph[j][1],safe)
                elif graph[j][1] == root and graph[j][0] != root:
                    dfs(graph[j][0],safe)
                    
            return 
        
        
        
       
        count = 0
        """ driver code"""
        safe = set()
        visited = set()
        for i in range(n):
            if i in safe:
                continue
            count += 1
            dfs(i,safe)
            
     
        
        """ answer finalization """
        
        return count