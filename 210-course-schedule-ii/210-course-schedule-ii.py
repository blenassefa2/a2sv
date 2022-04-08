class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dic = {}
    
        for ele in prerequisites:
            if ele[0] not in dic:
                dic[ele[0]] = 1
            else:
                dic[ele[0]] +=1
            if ele[1] not in dic:
                dic[ele[1]] = 0
        for i in range(numCourses):
            if i not in dic:
                dic[i] = 0
       
                
        queue = deque()
        visited = []
        for ele in dic:
            if dic[ele] == 0:
                queue.append(ele)
                
        while queue:
            curr = queue.popleft()
            visited.append(curr)
            
            for i in range(len(prerequisites)):
                if curr == prerequisites[i][1]:
                    dic[prerequisites[i][0]]-=1
                    if dic[prerequisites[i][0]] == 0:
                        queue.append(prerequisites[i][0])
           
        a = []
        if len(prerequisites) == 0:
            for i in range(numCourses):
                a.append(i)
            return a       
        if len(visited) == len(dic):
            return visited
        
        
        return a
        