class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        def recur(i, value):
            print(i,value)
            if i < 0:
                return n -1
            current = recur(i - 1, s[i - 1])
            
            s[current] = value
            return current - 1
        
        recur(n - 1,s[-1])
        
        print(s)