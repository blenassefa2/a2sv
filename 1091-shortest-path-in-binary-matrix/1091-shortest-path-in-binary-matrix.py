class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
     
        visited = set()
        inbound = lambda x: 0 <= x[0]< len(grid) and 0<=x[1] < len(grid)
        Dir = [[1,0],[0,1],[-1,0],[0,-1],[1,1],[-1,-1],[-1,1],[1,-1]]
        queue = deque([[[0,0], 0]]) #we are starting from top corner
        
        while queue:
            
            [currX, currY], length = queue.popleft()
            if (currX, currY) in visited:
                continue
            if grid[currX][currY] == 1:
                continue
            
            if currX == currY == len(grid)-1:
                return length + 1
            visited.add((currX,currY))
            for dx,dy in Dir:
                newX, newY = dx + currX, dy +currY
                
                if (newX,newY) not in visited and inbound((newX, newY)) and grid[newX][newY]==0:
                    queue.append([[newX,newY], length + 1])
        return -1