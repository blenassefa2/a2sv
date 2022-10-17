class Solution:
    __dp = defaultdict()
 
    def recurse(self, current: str, index: int, original: str) -> bool:
        
        if index >= len(original):
            return not current
        
        if (current, index,original) in Solution.__dp:
            return Solution.__dp[(current, index,original)]
        answer = True
        if original[index]  == ")":
            
            if current == "":
                answer = False
            else:
                future = self.recurse(current[:-1], index + 1, original)
                answer = answer and future
                
        elif original[index] == "(":
            future = self.recurse(current + "(", index + 1, original)
            answer = answer and future
        else:
            
            future1 = self.recurse(current+"(", index + 1, original)
            future2 = self.recurse(current, index + 1, original)
            future3 = self.recurse(current[:-1], index + 1, original)
            
            answer = answer and future1 or future2 or future3
            
        Solution.__dp[(current, index,original)] = answer    
        return answer
        
        
    def checkValidString(self, s: str) -> bool:
        
        answer = self.recurse("", 0, s)
        return answer
        
        
        