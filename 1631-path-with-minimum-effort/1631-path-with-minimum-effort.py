class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n,m = len(heights), len(heights[0])
        inbound = lambda x,y: 0<= x<n and 0<=y<m
        Dir = [[1,0],[0,1],[-1,0],[0,-1]]
        
        self.ans = inf
        def recurse(i,j,effort,bigger,visited):
            if bigger < effort:
                return False
            if (i,j) in visited:
                return False
            if i == n -1 and j == m - 1:
                return True
            visited.add((i,j))
            for d in Dir:
                n_i,n_j = i + d[0] , j + d[1]
                
                if inbound(n_i,n_j):
                    a = max(effort, abs(heights[i][j] - heights[n_i][n_j]))
                    
                    if recurse(n_i,n_j, a, bigger , visited):
                        return True
            # visited.remove((i,j))
            return False
            
        l,r = 0, 1000000
        best = r
        while l <= r:
            mid = (l+r)//2
            
            if recurse(0,0,-inf,mid,set()):
                best = mid
                r = mid - 1
            else:
                l = mid + 1
        return best