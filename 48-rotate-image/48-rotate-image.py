class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        
        [[5,1,9,5],
         [2,4,8,1],
         [13,3,6,9],
         [16,7,10,11]]
        
        [11,12,14,15]
        """
        n = len(matrix)
        new = []
        
        for i in range(n):
            a = []
            for j in range(n-1, -1, -1):
                a.append(matrix[j][i])
            new.append(a)
    
        for i in range(n):
            for j in range(n):
                matrix[i][j] = new[i][j]
        