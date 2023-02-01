class Solution:
   
    def dp(self, current, values, store):
        if current >= len(values):
            return 0
        
        if current in store:
            return store[current]
        
        currentAge, currentScore = values[current]
        take = 0
        for i in range(current +1, len(values)):
            if currentScore <= values[i][1]:
                take = max(take, self.dp(i, values, store))
            
        store[current] = take + currentScore
        
        return take +currentScore
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        """
        intuition:
        ---------
        
        the question is asking us to find un increasing sub sequence of (x,y)
        where x is score and y is age 
        
        so we should sort  them with age and try to find increasing sub sequence
        of scores
        
        
        to do this we can use recursion and memorization
        
        state: index, previousScore
        
        termination point: index > len(scores)
        
        let n be len(scores) == len(age)
        
        Time Complexity = n^2
        
        Space Complexity = n^2
        
        
        """
        # initialize variables
        final = 0
        values = []
        visited = defaultdict(int)
        for i in range(len(scores)):
            values.append((ages[i], scores[i]))
        
        #sort
        values.sort()
        
        #perform recursion and return answer
        
        """Driver code"""
        for i in range(len(scores)):
            final = max(final, self.dp(i,tuple(values), visited))
        
        
        return final 
    
        