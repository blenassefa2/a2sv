class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        li = [x for x in range(1,n+1)]
        i = 0
    
        while(len(li) >1):
            temp = (k%(len(li)))-1
            i = (i + temp) % len(li)
            li.remove(li[i])
        
        return(li[0])
        