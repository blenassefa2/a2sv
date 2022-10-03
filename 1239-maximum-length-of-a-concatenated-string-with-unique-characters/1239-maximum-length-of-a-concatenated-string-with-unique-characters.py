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
        """

        def recurse(curr,i):
            if len(set(curr)) != len(curr):
                return 0
            ans = len(curr)
            for j in range(i, len(arr)):
                ans = max(ans, recurse(curr+arr[j],j))
            return ans
        return recurse('',0)