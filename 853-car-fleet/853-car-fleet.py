class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        x = [(position[i],speed[i]) for i in range(len(speed))]
        
        x.sort()
        fleet = 0
        current_time = -1
        for  i  in range(len(speed) - 1, -1, -1):
            
            time = (target - x[i][0])/ x[i][1]
            
            if time > current_time:
                current_time = time
                fleet += 1
        
        return fleet