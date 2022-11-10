class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        slopes = defaultdict(set)
        verticalLines = defaultdict(set)
        horizontalLines = defaultdict(set)
        maximumSlope = 1
        
        for x0, y0 in points:
            for x1,y1 in points:
                if not(x0==x1 and y0 == y1):
                    
                    if x0 != x1 and y0 != y1:
                        
                        currentSlope = (y1 - y0) / (x1-x0)
                        currentIntercept = y0 - (currentSlope*x0)
                        
                        slopes[(currentSlope,currentIntercept)].add((x0,y0))
                        slopes[(currentSlope,currentIntercept)].add((x1,y1))
                        maximumSlope = max(maximumSlope, len(slopes[(currentSlope,currentIntercept)]))
                    elif x0 == x1:
                        verticalLines[x0].add(y1)
                        verticalLines[x0].add(y0)
                    
                        maximumSlope = max(maximumSlope, len(verticalLines[x0]))
                    elif y0 == y1:
                        horizontalLines[y0].add(x1)
                        horizontalLines[y0].add(x0)
                    
                        maximumSlope = max(maximumSlope, len(horizontalLines[x0]))
       
      
        return maximumSlope