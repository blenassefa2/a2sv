class Solution:
    def nextGreaterElement(self, n: int) -> int:
        """
        we have two scenarios:
        
            if the digits of the number are decreasing: eg n = 4321
                 we can't form any number greater than n with permutation of the digits
            
            if there are atleast two digits that are not decreasing:eg n = 58765
                find the first occurence of increasing sequence
                    swap it with the nearest smallest value
                    reverse the decreasing values upto this point to increasing   
                    
            let k be --> number of digits
            Time complexity  O(n)
            Space complexity O(n)
        """
        
        s = list(str(n))
        stack =[len(s) -1]
        i = len(s) - 2
        while  i >= 0 and s[stack[-1]] <= s[i]:
            stack.append(i)
            i -= 1
        else:
            if len(stack) == len(s):
                return -1
            b = s[i]
            j = i
            while stack and  s[stack[-1]] > b: 
                j = stack.pop()
            s[i], s[j] = s[j], s[i]
            ans =int("".join(s[:i+1]) + "".join(sorted(s[i+1:])))
        
            return ans if ans <= 2147483647 else -1