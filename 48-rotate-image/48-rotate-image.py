class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        
        [1,2,3],
        [4,5,6],      1, 2 => 2,1
        [7,8,9]      
        
        [1,4,7]
        [2,5,8]
        [3,6,9]
        
        
        
        """
        n = len(matrix) -1
        changed = set()
        for i in range(n+1):
            for j in range(n+1):
                if (i,j) in changed:
                    continue
                changed.add((i,j))
                changed.add((j, abs(i-n)))
                matrix[i][j], matrix[j][abs(i-n)] = matrix[j][abs(i-n)], matrix[i][j]
        
       
        