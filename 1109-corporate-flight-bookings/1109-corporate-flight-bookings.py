class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        line = [0]*(n+1)
        for f,l,s in bookings:
            line[f-1] += s
            line[l] -= s
        for i in range(1,len(line)):
            line[i] = line[i -1] + line[i]
        
        return line[:-1]