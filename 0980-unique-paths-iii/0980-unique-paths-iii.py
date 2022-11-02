class Solution:
    def inBound(self, currX,currY,grid):
        return 0<= currX<len(grid) and 0<= currY<len(grid[0])
    
    def dfs(self, currX,currY,grid, visited,Dir,totalOpen):
        if not self.inBound(currX,currY,grid):
            return 0
        if (currX,currY) in visited:
            return 0
        if grid[currX][currY] == -1:
            return 0
        if grid[currX][currY] == 2:
            
            return 1 if len(visited) == totalOpen+1 else 0
       
      
        visited.add((currX,currY))
        answer = 0
        for d in Dir:
            newX, newY = currX + d[0], currY+d[1]
            answer += self.dfs(newX,newY,grid,visited,Dir,totalOpen)
        visited.remove((currX,currY))
        return answer
        
        
        
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        Dir = [[1,0],[0,1],[-1,0],[0,-1]]
        startX,startY = 0,0
        totalOpen = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    startX,startY = i,j
                elif grid[i][j] == 0:
                    totalOpen += 1
       
        return self.dfs(startX,startY,grid,set(),Dir, totalOpen)
                    