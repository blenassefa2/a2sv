class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        tup = []
        
        for x in range(len(difficulty)):
            tup.append((profit[x], difficulty[x]))
        
        tup.sort(key = lambda x:( x[0], x[1]))
        
        
        worker.sort()
        ans = 0
        
        for i in range(len(difficulty) -1, -1, -1):
            while worker and worker[-1] >= tup[i][1]:
                worker.pop()
                ans += tup[i][0]
        return ans
            
            