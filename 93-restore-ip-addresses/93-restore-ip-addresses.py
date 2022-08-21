class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        if len(s) < 4:
            return []
        
        self.ans = set()
        
        not_num = lambda x: x[0] == "0" and len(x) > 1
        gt_255 = lambda y: int(y) > 255
        
        def helper(b1,b2,b3):
            a,b,c,d = s[:b1], s[b1:b2], s[b2:b3], s[b3:]
            if not a or not b or not c or not d:
                return ""
            if not_num(a) or not_num(b) or not_num(c) or not_num(d):
                return ""
            if gt_255(a) or gt_255(b) or gt_255(c) or gt_255(d):
                return ""
            
            return a + "." + b + "." + c + "." + d
        
        
        
            
                
                
        for i in range(0, len(s)):
            for j in range(1, len(s)):
                for k in range(2, len(s)):
                    tmp = helper(i,j,k)
                    if tmp:
                        self.ans.add(tmp)
                        
       
        return(self.ans)