class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        we are going to recurse starting from a single open parenthesis
        
        for the base case we want 
            #of '(' == n and #of '(' == #of')'
        
        for normal cases there are two routes
            1. #of '(' > #of ')' 
                in which case we can add ')'
            2. #of '(' < n
                in which case we can add '('
        
        
        """
        self.ans = []
        def recurse(curr, openCount, closedCount):
            if openCount == closedCount and openCount == n:
                self.ans.append(curr)
                return
            
            if openCount > closedCount:
                recurse(curr + ')', openCount, closedCount + 1)
            if openCount <n:
                recurse(curr +'(', openCount + 1, closedCount)
            return
        recurse('(',1,0)
        return self.ans
        
     