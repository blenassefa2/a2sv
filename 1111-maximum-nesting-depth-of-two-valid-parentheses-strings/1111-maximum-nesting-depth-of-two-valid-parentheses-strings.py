class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        """
        conditions for an answer:
                a, b must be vps
                a.len + b.len = seq.len
                max(depth(a), depth(b)) <= all the rest
        
        "(()())"
             |
        ans =  "11110"
        [("(", 0)]
        
        
        ans  = [-1] * leng( seq)
        
        stack = [(0, 0)]
        
        i  = 0
        
        while i < len(seq):
        
            if !stack:
                stack.append((i, 0))
                i += 1
                continue
                
            if seq[i] == "(":
                if stack[-1][1] ==0:
                    stack.append((i, 1))
                else:
                    stack.append((i, 0)
            else:
                index, state = stack.pop()
                
                ans[index], ans[i] = state,state
                
            i+= 1
    

        """
        
        
        
        
        ans  = [-1] * len(seq)
        
        stack = [(0, 0)]
        
        i  = 0
        
        while i < len(seq):
        
            if not stack:
                stack.append((i, 0))
                i += 1
                continue
                
            if seq[i] == "(":
                if stack[-1][1] ==0:
                    stack.append((i, 1))
                else:
                    stack.append((i, 0))
            else:
                index, state = stack.pop()
                
                ans[index], ans[i] = state,state
                
            i+= 1
                                 
        return(ans)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        