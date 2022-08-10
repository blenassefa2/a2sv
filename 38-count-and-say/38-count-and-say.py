class Solution:
    def countAndSay(self, n: int) -> str:
        def conv(s):
            nw =""
            count = 0
            num = s[0]
            
            l = 0
            r = 0
            while r < len(s):
                while r< len(s) and s[r] == num:
                    r += 1
                    count += 1
                
                nw += str(count) + str(num)
                count = 0
                if r < len(s):
                    num = s[r]
                l = r
                
            return nw
                
        
        def recurs(dist):
            if dist == 1:
                return "1"
            
            return conv(recurs(dist - 1))
        
        return recurs(n)