class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        """
        so what we do is simple backtracking with two possibilites at each index
        state index, currstring
            1, remove it
            2, not remove it
        if the current index > len(s): check validity of the new formed string then             depending on its length change your final answer 
        """
        self.final = []
        def valid(w):
            stack = []
            for i in range(len(w)):
                if w[i] != "(" and w[i] != ")":
                    continue
                if w[i] == "(":
                    stack.append("(")
                else:
                    if not stack:
                        return i
                    else:
                        if stack[-1] == "(":
                            stack.pop()
                        else:
                            return i
            return i if stack else -1
        def recurse(i, curr,dp):
            if(i,curr) in dp:
                return
            if i >= len(s):
                if valid(curr) == -1:
                    if not self.final or len(self.final[-1]) == len(curr):
                        self.final.append(curr)
                    elif len(self.final[-1]) < len(curr):
                        self.final = [curr]
                dp[(i,curr)] = 2
                return
            dp[(i,curr)] = 2
            if s[i] == ")" or s[i] == "(":
                recurse(i+1, curr,dp)
            recurse(i+1, curr + s[i],dp)
        
       
        recurse(0,"", defaultdict(int))
        return set(self.final)
        
        
                    
                    