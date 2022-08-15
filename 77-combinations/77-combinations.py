class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def recurs(a,curr):
            if a > n:
                return
            if len(curr) == k:
                ans.append(list(curr))
                return
            
            for i in range(a+1, n+1):
                
                curr.append(i)
                recurs(i, curr)
                curr.pop()
                
        
            
            
        recurs(0,[])
        return ans
            
            