class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        final = [[1], [1,1]]
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]
        for i in range(3,numRows+1):
            x = [1]
            for j in range(1,len(final[-1])):
                x.append(final[-1][j] + final[-1][j-1])
            x.append(1)
            final.append(x)
        return (final)