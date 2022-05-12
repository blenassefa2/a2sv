class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        
        for x in range(len(timePoints)):
            if timePoints[x][:2] == "00":
                timePoints[x] = "24" +timePoints[x][2:]
                
        
        
        timePoints.sort()
        best = 100000000000000000000000
        for i in range(len(timePoints) - 1):
            

            h1,m1 = timePoints[i].split(":")
            h2,m2 = timePoints[i + 1].split(":")

            
            h1,h2,m1,m2 = int(h1), int(h2), int(m1), int(m2)
            h2_h1 = (((h2 *60) + m2) - ((h1 * 60) +m1))
            best = min(best, h2_h1)
        
        h1,m1 = timePoints[0].split(":")
        h2,m2 = timePoints[-1].split(":")
        
        
        
        h1,h2,m1,m2 = int(h1), int(h2), int(m1), int(m2)
    
        return min(best,1440 -(((h2 *60) + m2) - ((h1 * 60) +m1 )))