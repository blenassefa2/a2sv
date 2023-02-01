class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        """
        intuition:
        
        the plant times are always going to be counted 
        and earliest day is always day >= sum(planttime) 
        
        
        so what we will try to minimize is the grow time
        in order to do that the approach I am using is growing the plant that needs maximum growth time first then the second maximum and so on
        
        
        This will help us create more overlapp between planttime of plantx and plantx+1
        
        
        """
        
        # Initialize variables:
        final = 0
        previousPlantEnd = 0
        time = [[growTime[i],plantTime[i]] for i in range(len(plantTime))]
        
        
        # Sort the time
        time.sort(key =lambda x: (-x[0], x[1]))
        
        
        # Form the final
        for index in range(len(time)):
            if not final:
                final = sum(time[index])
                previousPlantEnd = time[index][1]
            else:
                final = max(final, previousPlantEnd + sum(time[index]))
                previousPlantEnd += time[index][1]
                
        return final
                
                
                
        
        