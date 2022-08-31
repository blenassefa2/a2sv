class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        inDegrees = [0]*numCourses
        outDegrees = defaultdict(list)
        qu = deque([])
        
        for i, o in prerequisites:
            inDegrees[o] += 1
            outDegrees[i].append(o)
            
        for i in range(numCourses):
            if inDegrees[i] == 0:
                qu.append(i)
        total = 0       
        while qu:
            n = qu.popleft()
            total += 1
            for i in outDegrees[n]:
                inDegrees[i] -= 1
                
                if not inDegrees[i]:
                    qu.append(i)
                    
        return total == numCourses
        
        