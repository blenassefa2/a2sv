class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = [0]*numCourses
        outDegrees = defaultdict(set)
        
        for i,o in prerequisites:
            outDegrees[i].add(o)
            
        def recurs(node, dp):
            if node in dp:
                return dp[node]

            if visited[node] == 1:
                dp[node] = False
                return False
            
            ans = True
            visited[node] = 1
            for n in outDegrees[node]:
                ans = ans and recurs(n,dp)
            
            dp[node] = ans
            visited[node] = 0
            return ans
            
            
        
        """Driver code"""
        
        for i in range(numCourses):
            if visited[i] == 0:
                if not recurs(i,defaultdict()):
                    return False
        return True