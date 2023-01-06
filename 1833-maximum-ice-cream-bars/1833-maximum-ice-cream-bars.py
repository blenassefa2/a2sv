class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
       
        bought = 0
        for i in costs:
            coins -= i
            if coins >= 0:
                bought += 1
                
            
            
        return bought
        
        