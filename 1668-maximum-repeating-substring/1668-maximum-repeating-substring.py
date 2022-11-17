class Solution:
    def findAll(self, sequence,pattern):
        final = []
        current = ""
        index = 0
        for index,value in enumerate(sequence):
            if len(current) == len(pattern):
                if current == pattern:
                    final.append(index - len(pattern))
                current = current[1:]
            current += value
       
        if current == pattern:
            final.append(index - len(pattern) + 1)
        return final

    def maxRepeating(self, sequence: str, word: str) -> int:
        indicies = self.findAll(sequence,word)
        # print(indicies)
        final = 0
        search = set(indicies)
        for i in indicies:
            current = 0
            currentI = i
            while currentI in search:
                current += 1
                currentI += len(word)
            final = max(final, current)
            
        return final
                