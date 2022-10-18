class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        """
        8:58
        9:21
        1:34
        """ 
        # initialize the answer array
        answer = [itself for itself in range(len(quiet))]
        
        # create the edges
        edges = defaultdict(list)
        indegree = [0]*len(quiet)
        
        for rich,poor in richer:
            edges[rich].append(poor)
            indegree[poor] += 1
            
        # build the dependency in an array ith index will have quitest person that have equal or more money than person i
        #construct queue
        qu = deque()
        for person in range(len(quiet)):
            if indegree[person] == 0:
                qu.append(person)
        
        while qu:
            
            N = len(qu)
            for _ in range(N):
                node = qu.popleft()
                    

                for poorer in edges[node]:
                    
                    indegree[poorer] -= 1

                    answer[poorer] = min(answer[node], answer[poorer], key = lambda x:quiet[x])


                    if indegree[poorer] == 0:
                        qu.append(poorer)
                        
        # return the built array
    
        return answer
        
        