class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        """
        simulation
        """
        time = 0
        
        while True:
            
            for i in range(len(tickets)):
                if tickets[i] > 0:
                    time += 1
                    
                    tickets[i] -= 1
                
                if tickets[k] == 0:
                    return time
                
                
        