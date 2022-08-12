class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        
        """
        if original_color === color:
            return grid
            
        Dir = [[1,0], [0,1], [-1,0], [0,-1]]
        
        func(m,n, visited)
            base case:
                m,n out of grid --> return False
                m,n already visited --> return True
                grid[m][n] != original_color --> False

                ans = True
                for d in dir:
                    ans = ans and func(d+l(m,n))
                
                if not ans:
                    grid[m][n] = color
                
                return True
        
        """
        if grid[row][col] == color:
            return grid
        
        n,m = len(grid), len(grid[0])
        
        in_bound = lambda x: 0<=x[0]<n and 0<=x[1]<m
        Dir = [[1,0], [0,1], [-1,0], [0,-1]]
        
        def func(x,y, visited, original_color, color):
            if not in_bound([x,y]):
                return False
            if (x,y) in visited:
                return True
            if grid[x][y] != original_color:
                return False
            visited.add((x,y))
            print(visited)
            ans = True
            for a,b in Dir:
                n_x,n_y = a+x, b+y
                nw = func(n_x, n_y, visited, original_color,color)
                
                
                ans = ans and nw
            
            if not ans:
                grid[x][y] = color
               
            
            return True
        
        func(row,col, set(),grid[row][col], color)
        return grid