class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        """
        This one is also more like simulation
        
        first calculate uam
         
        then for each uam count populate answer
        """
        # initialize variables
        answer = [0] * k
        uam = defaultdict(set)
        
        
        # calculate UAM
        for id_, minuite in logs:
            uam[id_].add(minuite)
        
        
        # populate answer
        for id_ in uam:
            if len(uam[id_]) <= k:
                answer[(len(uam[id_]) - 1)] += 1
                
                
        return answer
         