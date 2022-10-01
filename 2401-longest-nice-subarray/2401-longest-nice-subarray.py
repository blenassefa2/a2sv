class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        def valid(b,t,v):
            
            for i in range(v):
                if t[i] - b[i] > 1:
                    return False
            return True
        max_=max(nums)
        val = int(floor(log2(max_)) + 3)
        prf = [[0]*val]

        all_ =[] 
        
        for i in nums:
            a = [0]*val
            x = i
            while x:
                b = (x&(x - 1))
                a[val -1 -int(log2(x^b))] += 1
                x = b
            all_.append(a)
            prf.append([prf[-1][j] + a[j] for j in range(val)])
       
    
        qu = deque()
        final = 0
        for i in range(len(prf)):
            
            
            while qu and not valid(prf[qu[0]],prf[i],val):
                
                qu.popleft()
                
            qu.append(i)
            final = max(final, len(qu)-1)
        return final
        
            
            
        
        