class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        for i in range(len(ops)):
            
            if ops[i].isdigit() or ops[i][1:].isdigit():       
                x = int(ops[i])
                stack.append(x)
            elif ops[i] == "+":
                stack.append(stack[-1] + stack[-2])
            elif ops[i] == "D":
                stack.append(stack[-1] * 2)
            elif ops[i] == "C":
                stack.pop()
    
        return sum(stack)