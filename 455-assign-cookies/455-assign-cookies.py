class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        '''
        counter: 3
        g = [1,7,8,8]  
                   |
        s = [1,4,4,5,5,7,7,7,7,9] 
                                  | 
        n = len(g)
        m = len(s)
        t = O(nlg(n) + mlg(m))
        '''
        
        
        g.sort()
        s.sort()
        
        content = 0
        child, cookie = 0, 0
        
        
        while child < len(g):
            
            satisfied  = False
            
            while cookie < len(s):
                if s[cookie] >= g[child]:
                    content += 1
                    cookie += 1
                    satisfied = True
                    break
                cookie += 1
            if not satisfied:
                break
            child += 1
                
        return content