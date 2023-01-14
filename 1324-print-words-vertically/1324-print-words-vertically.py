class Solution:
    def printVertically(self, s: str) -> List[str]:
        l = s.split(" ")
        
        maxLength = 0
        
        for word in l:
            maxLength = max(maxLength, len(word))
            
        for i in range(len(l)):
            if len(l[i]) < maxLength:
                l[i] = l[i] + "*"*(maxLength - len(l[i]))
                
        final = []
        for i in range(maxLength):
            answer = []
            for j in range(len(l)):
                answer.append(l[j][i])
             
            for k in range(len(answer) - 1, -1, -1):
                if answer[k] == "*":
                    answer[k] = ""
                else:
                    break
            for k in range(len(answer) - 1, -1, -1):
                if answer[k] == "*":
                    answer[k] = " "
                
                    
            final.append("".join(answer))
            
        return final