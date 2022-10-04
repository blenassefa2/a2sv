class Solution:
    def maxLength(self, arr: List[str]) -> int:
        """
        I am going to recurse throught the whole arr checking for combinations
        
        states current built up string==> curr, current index==> i
        
        there are one base case:
            1. if built up string contains duplicate letters
                return 0
            
        
        other than the base case we iterate from i to len(arr)
            call the function with new curr and i and store the result if it is max length
        
         Time complexity => O(n!)
         space complexity => O(n!) if you consider the stack
         I got it reduced to tc-> O(n) sc -> O(n)if you consider the stack
         
         by using backtracking and dp
         instead of recursing for all possible combination that works with i
         
         I keeptrack of a string and check two possibilities of including or not including i
         
        """

        def recurse(curr,i,dp):
            if len(set(curr)) != len(curr):
                return 0
            if i >= len(arr):
                return len(curr)
            if (curr,i) not in dp:
                dp[(curr,i)] =  max(recurse(curr+arr[i],i+1,dp), recurse(curr, i+1,dp))
                
            return dp[(curr,i)] 
             
            
        return recurse('',0,defaultdict(int))