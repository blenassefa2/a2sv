class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        """
        I keep track of the indecies I matched with i
            if  the top of the stack is not equal with target[i] 
                i will stay on that index
                ans the top of the stack is popepd
            else i will move on to the next i + 1
            
        
        """
       
        ans = []
        stack = []
        
        i = 0
        for k in range(1,target[-1]+1):
            
            if not stack: 
                stack.append(k)
                ans.append("Push")
    
            elif stack and i < len(target) and stack[-1] != target[i]:
                stack.pop()
                ans.append("Pop")
                stack.append(k)
                ans.append("Push")
            elif stack and i < len(target) and stack[-1] == target[i]:
                stack.append(k)
                ans.append("Push")
                i += 1
              
        return ans