class Solution:
    def largestInteger(self, num: int) -> int:
        ls = list(str(num))
    
        odd = deque([])
        even = deque([])
        counter = [0]*10
        
        for i in range(len(ls)):
            counter[int(ls[i])] += 1
            if int(ls[i]) % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        j = 9
        nw = ["0"]*len(ls)
        while j >=0:
            if counter[j] >= 1:
                if j %2 == 0:
                    nw[even.popleft()] = str(j)
                else:
                    nw[odd.popleft()] = str(j)
                counter[j] -= 1
                continue
            j -= 1
        
       
        return int("".join(nw))
        