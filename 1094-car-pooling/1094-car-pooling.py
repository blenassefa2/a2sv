class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x: (x[1],x[2]))
        llength = trips[-1][2]
        for w, i ,j in trips:
            llength = max(llength, j)
        line = [0]*(llength+1)
        
        for n,f,t in trips:
            line[f] += n
            line[t] -= n
        for i in range(1,len(line)):
            line[i] = line[i] + line[i-1]
        return max(line) <=capacity