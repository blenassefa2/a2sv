class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if not n:
            return 0
        memory = [0, 1]
        i = 2
        while i < n + 1:
            if i % 2 == 0:
                memory.append(memory[i // 2])
            else:
                x= (i - 1)// 2
                memory.append(memory[x] +memory[x + 1])
            i += 1
                
        return max(memory)
        