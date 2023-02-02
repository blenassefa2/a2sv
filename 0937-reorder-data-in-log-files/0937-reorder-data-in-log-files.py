class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters = []
        digits = []
        for i in range(len(logs)):            
            l = logs[i].split(" ")
            identifire = l[0]
            l = l[1:]
            isDigit = True
            for val in l:
                if not val.isdigit():
                    isDigit = False
            if not isDigit:
                letters.append(logs[i])
            else:
                digits.append(logs[i])
        letters.sort(key=lambda x: (" ".join(x.split()[1:]), x.split()[0]))
        
        
        letters.extend(digits)
        return letters