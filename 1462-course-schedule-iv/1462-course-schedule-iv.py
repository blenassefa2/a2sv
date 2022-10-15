class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        indeg = defaultdict(list)
        outdegree =[0]*numCourses
        for i,j in prerequisites:
            indeg[j].append(i)
            outdegree[i] += 1
            
        dependants = defaultdict(set)
        
        qu = deque()
        for i in range(numCourses):
            if outdegree[i] == 0:
                qu.append(i)
       
        while qu:
            node = qu.popleft()
            
            val = set()
            val = val.union(dependants[node])
            val.add(node)
            for i in indeg[node]:
                outdegree[i] -= 1 
                dependants[i] = dependants[i].union(val)
                if outdegree[i] == 0:
                    qu.append(i)
            
            
        
       
        ans = []
        # for k in dependants:
        #     print(k,dependants[k])
        for i,j in queries:
            ans.append((j in dependants[i]))
        return ans
            
            
            