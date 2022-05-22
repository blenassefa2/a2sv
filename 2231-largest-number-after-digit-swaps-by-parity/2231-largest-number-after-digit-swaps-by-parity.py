class Solution:
    def largestInteger(self, num: int) -> int:
        ls = list(str(num))
    
        odd = deque([])
        even = deque([])
        
        for i in range(len(ls)):
            if int(ls[i]) % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        ls.sort(reverse=True)
        
        nw = ["0"]*len(ls)
        for j in range(len(ls)):
            x = int(ls[j])
            if x %2 == 0:
                nw[even.popleft()] = ls[j]
            else:
                nw[odd.popleft()] = ls[j]
        return int("".join(nw))
        