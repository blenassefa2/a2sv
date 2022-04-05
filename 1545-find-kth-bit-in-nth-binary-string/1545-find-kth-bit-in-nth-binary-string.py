class Solution:
    def recur(self, s, n):
        if n == 0:
    
            return "0"
        t = self.recur(s, n -1)
        
        n = 1<<len(t)
        N = int(t,2) 

        x = int(n)-(N)-1 
        y = f'{x:b}'
        if len(t) <len(y):
            a = (len(y) - len(t))
            y = ((f'{1<<a:b}' + f'{x:b}')[1:])
        
        z = y[::-1]
        
        return  t + "1" + z
    def findKthBit(self, n: int, k: int) -> str:
        t = self.recur("",n)
        return t[k-1]