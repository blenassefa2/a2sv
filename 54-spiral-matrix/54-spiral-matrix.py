class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        visited = set()
        lis = []
        n,m = len(matrix), len(matrix[0])
        
        Dir = [(0,1), (1,0), (0,-1), (-1,0)]
        
        i, d, pos = 1, 0, (0,0)
        
        while i <=(n*m):
             
            visited.add(pos)
            lis.append(matrix[pos[0]][pos[1]])
            i += 1
            
            x , y = pos[0] + Dir[d][0] , pos[1] + Dir[d][1]
            if (x,y) in visited or x >= n or x < 0 or y <0 or y >= m:
                d += 1
                if d == 4:
                    d = 0
                pos = (pos[0] + Dir[d][0] , pos[1] + Dir[d][1])
            else:
                pos = (x,y)
            
        return (lis)