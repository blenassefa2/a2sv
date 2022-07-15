class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.mat = []
        
        for i in range(len(matrix)):
            prefix = [0]
            for j in range(len(matrix[i])):
                prefix.append(prefix[-1] + matrix[i][j])
            self.mat.append(prefix)
        print(self.mat)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum_ = 0
        for i in range(row1, row2 + 1):
            sum_ += (self.mat[i][col2 + 1] - self.mat[i][col1])
        return sum_

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)