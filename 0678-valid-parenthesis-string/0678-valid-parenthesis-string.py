class Solution:
    def checkValidString(self, s: str) -> bool:
        
        # initialize my two stacks for the star and opening parenthesis
        open_parenthesis = []
        star = []
        
        for index, value in enumerate(s):
            
            if value == "(":
                open_parenthesis.append(index)
            elif value == "*":
                star.append(index)
            else:
                if not open_parenthesis and not star:
                    return False
                
                if open_parenthesis:
                    open_parenthesis.pop()
                else:
                    star.pop()
        
        while star and open_parenthesis:
            if star[-1] < open_parenthesis[-1]:
                return False
            
            star.pop()
            open_parenthesis.pop()
        
        return not open_parenthesis
        