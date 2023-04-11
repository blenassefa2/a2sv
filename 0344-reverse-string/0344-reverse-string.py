class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def recurse(current, value):
            if current == -1:
                return len(s) -1
            
            place = recurse(current - 1, s[current - 1]) 
            s[place] = value
            
            return place - 1
        
        recurse(len(s) - 1, s[-1])