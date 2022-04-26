class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        self.days = len(prices)
        visited = set()
        def dfs(a):
            if a + 1 >= len(prices):
                return 0
            visited.add(a)
            
            if prices[a] != prices[a + 1] +1:
                return 0
            count = dfs(a+1) +1
            self.days += count
            return count
        for i in range(len(prices)):
            if i not in visited:    
                dfs(i)
        return (self.days)