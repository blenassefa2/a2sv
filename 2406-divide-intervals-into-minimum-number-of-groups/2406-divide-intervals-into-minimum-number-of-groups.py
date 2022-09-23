class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        llength = -1
        
        
            
        line= []
        
        for l,r in intervals:
            line.append([l,'b'])
            line.append([r, 'e'])
        line.sort()
        final = 0
        s = 0
        for i in range(len(line)):
            if line[i][1] == "b":
                s += 1
            else:
                s -=1
            final = max(final, s)
        
        return final