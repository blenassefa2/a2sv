class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        Dir  = [[0,1],[1,0]]
        if obstacleGrid[0][0] == 1:
            return 0
       
        n,m = len(obstacleGrid), len(obstacleGrid[0])
    
        @cache
        def dfs(node,total):
            if node[0] == n -1 and node[1] == m -1:
                total += 1
                return total
            t = 0
            for d in Dir:
                x,y = node[0] + d[0], node[1] + d[1]
                if (0 <= x< n and 0 <= y < m) and obstacleGrid[x][y] == 0:
                    t += dfs((x,y),total)
            return t
        return(dfs((0,0),0))
        