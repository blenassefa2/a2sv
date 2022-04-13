class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        children = defaultdict(list)
        nums = [0] * (n + 1)
        
        for i,j in relations:
            nums[i] += 1
            children[j].append(i)
     

        qu = deque()
        for k in range(1,len(nums)):
            if nums[k] == 0:
                qu.append(k)
       
        self.final = 0
        self.dp = defaultdict()
        
        """DFS code"""
        def dfs(m):
            if m not in children:
                self.final = max(self.final,time[m-1])
                return time[m - 1]
            
            if m in self.dp:
                return self.dp[m]
           
            a = 0
        
            for x in children[m]:
                a = max(a, dfs(x))
                
            
            
            self.dp[m] = time[m - 1] + a  
            
            self.final = max(self.final,self.dp[m])
           
            return self.dp[m]
                
                
                
        """Driver code"""
        
        for l in qu:
            dfs(l)
         
        return self.final