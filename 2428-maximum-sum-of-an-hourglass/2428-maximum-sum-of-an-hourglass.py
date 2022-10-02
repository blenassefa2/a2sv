class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        """
        first build a prefix sum so it will be easier to get the sums
        
        then go for calculating each hourglass on third column for every third row 
        
        while calculating an hourglass also keep track of the maximum and return it finally
        
        """
        n,m = len(grid[0]), len(grid)
        presum = []
        
        for i in range(m):
            row = [0]
            for j in range(n):
                row.append(row[-1] +grid[i][j])
            presum.append(row)
        
        final = 0
        
        for i in range(2, len(presum)):
            
            for j in range(3, len(presum[0])):
                rbx, rby = i,j
                rtx,rty = i -2, j
                ltx, lty = rtx,rty -3
                lbx,lby = i,j-3
                # print((presum[i][j], presum[i][j-3]),(presum[i-2][j] ,presum[i-2][j-3]), grid[i-1][j-2])
                final = max(final, (presum[i][j] - presum[i][j-3]) +(presum[i-2][j] -presum[i-2][j-3])+ grid[i-1][j-2])
        return final
        
        
                