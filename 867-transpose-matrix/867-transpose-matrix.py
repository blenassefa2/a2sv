class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n,m = len(matrix), len(matrix[0])
        ans =[]
        for i in range(m):
            tmp = []
            for j in range(n):
                tmp.append(matrix[j][i])
            ans.append(tmp)
        return ans
                