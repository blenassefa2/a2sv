class Solution:
    def robotWithString(self, s: str) -> str:
        # initialize variables
        smallestAfterMe = [""]*len(s)
        printed = []
        t = []
        index = 0
        
        # populate smallestAfterMe data
        smallestAfterMe[-1] = s[-1]
        for i in range(len(s) - 2, -1, -1):
            smallestAfterMe[i] = min(smallestAfterMe[i + 1], s[i])
        
        # Iterate through s choosing what to print and printing
        while index < len(s):
            if not t:
                t.append(s[index])
                index += 1
                continue
            while index < len(s) and t and  t[-1] > smallestAfterMe[index]:
                t.append(s[index])
                index += 1
            
            if t:
                printed.append(t.pop())
        while t:
            printed.append(t.pop())
        return "".join(printed)