class Solution:
    def topSort(self, graph: List[List[int]], k: int) -> List[int]:
        
        edges = defaultdict(list)
        indegree = [0]*(k+1)
        
        levels = []
        heapify(levels)
        sorted_array = []
        
        # create the edges and count indegree
        for previous, next_ in graph:
            edges[previous].append(next_)
            indegree[next_] += 1
        
        # initialize queue
        queue = deque()
        
        for node in range(len(indegree)):
            if indegree[node] == 0:
                queue.append(node)
                
        # initialize the level and continue the bfs
        processed = 0
        level = 0
        while queue:
            
            N = len(queue)
            
            for _ in range(N):
                
                current = queue.popleft()
                heappush(levels, (level,current))
                
                processed += 1
                
                for successor in edges[current]:
                    indegree[successor] -= 1
                    if indegree[successor] == 0:
                        queue.append(successor)

            level += 1
          
        # check if there was cycle detected
        if processed == k+1:
           
            # construct my sorted_array and return it
            while levels:
                sorted_array.append(heappop(levels)[1])
        
        return sorted_array
        
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        """
        
        1r -->2r--> 3r--> ...--> kr  
         0     1     2           k -1
        2c -->1c -->3c -->...--> kc
        
                      
        Input: k = 3, rowConditions = [[1,2],[3,2]], colConditions = [[2,1],[3,2]]
        
       0 1--> 2 1
           /
         3 0
          1 2 3
         [0 1 0]
         [1 3 2]
         
         
        row:    1  3   2
                0  1   2
        column: 3  2   1
        
        
        0 0 1
        3 0 0
        0 2 0
        
        """
        # initialize my answer grid with zeros
        answer = []
        
        for i in range(k):
            
            cells = []
            for j in range(k):
                cells.append(0)
            
            answer.append(cells)
        
        # create the row graph and the column graph
        row_graph = self.topSort(rowConditions,k)[1:]
        column_graph = self.topSort(colConditions,k)[1:]
       
        # populate my answer grid with the actual answer by using the graph I created
        if row_graph and column_graph:
            position = defaultdict(list)

            for number in range(1,k+1):
                position[number].append(0)
                position[number].append(0)

            for index, value in enumerate(row_graph):
                position[value][0] = index

            for index, value in enumerate(column_graph):
                position[value][1] = index


            for number in range(1, k+1):
                row, col = position[number]
                answer[row][col] = number
        else:
            answer = []

        # return the answer
        return answer
        
       