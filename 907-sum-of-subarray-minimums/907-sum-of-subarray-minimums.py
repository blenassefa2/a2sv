class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        """
        I am going to use the concept of monotinic(increase) stack
        that is if somebody smaller than you is coming you are useless so your maximum ability will get counted and you will be poped out to never be remembered
        
        
        how does and index know the influence it made so far:
            (rb -i + 1)(i - lb + 1)
        
        
        on the stack we will be keeping track of the real index of the value and the recent index it forced out
        so it will be our lb for others in the future
        """
        arr.append(0)
        stack = []
        ans = 0
        for i, v in enumerate(arr):
            
            ni = i
            while stack and arr[stack[-1][0]] > v:
                c, lb = stack.pop()
                
                ans += ((i-c)*(c-lb+1)*arr[c])
                
                ni = lb
            
            stack.append([i, ni])
            
        return ans % 1000000007