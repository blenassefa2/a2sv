class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        self.final = 0
        
        def recurs(index, curr,visited):
            if (index,curr) in visited:
                self.final += visited[(index,curr)]
                return visited[(index,curr)]
            if curr == amount:
                self.final += 1
                return 1
            if curr > amount:
                return 0
            if index >= len(coins):
                return 0
            
            
            a = recurs(index, curr+coins[index],visited)
            b = recurs(index+1, curr, visited)
            
            
            
            visited[(index,curr)] += (a+b)
            return visited[(index,curr)]
            
        recurs(0,0,defaultdict(int))
        return self.final