class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        # initialize the variables
        prefix = [0]
        previousSteps = 0
        
        # build the prefix array
        for index,volume in enumerate(plants):
            if prefix[-1] > capacity:
                prefix.append(volume + plants[index - 1])
            else:
                prefix.append(prefix[-1] + volume)
                
        prefix = prefix[1:]
        
        # calculte the steps taken for each index 
        for index in range(len(prefix)):
            currentSteps = 1
            if prefix[index] > capacity:
                currentSteps += (index * 2)
            previousSteps += currentSteps
            
        # return the final number of steps
        return previousSteps