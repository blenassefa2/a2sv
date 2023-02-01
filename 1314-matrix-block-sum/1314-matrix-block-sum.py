class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        """
        intuition:
        ---------
        for each row we can calculate prefix sum and build prefix matrix
        
        for each answer[i][j]
        add the sums j - k to j + k of each row from i -k to i + k 
        
        let n be number of rows and m be number of columns
        Time complexity: O((n^2)*m)
        space complexity: O(n*m)
        
        """
        
        # initialize variables
        prefixMat = []
        answer = []
        
        
        # build prefix matrix
        for i in range(len(mat)):
            prefix = [0]
            for j in range(len(mat[0])):
                prefix.append(prefix[-1] + mat[i][j])
            prefixMat.append(prefix)
        
        # populate the answer
        for i in range(len(mat)):
            ansRow= []
            for j in range(len(mat[0])):
                total = 0
                leftTopRow = max(0, i - k)
                leftTopCol = max(0, j - k)
                rightBottomRow = min(len(mat) - 1, i + k)
                rightBottomCol = min(len(mat[0])-1, j + k)
                
                
                for row in range(leftTopRow,rightBottomRow + 1):
                    total += (prefixMat[row][rightBottomCol + 1] - prefixMat[row][leftTopCol])
                ansRow.append(total)
            answer.append(ansRow)
        
        # return answer
        return answer