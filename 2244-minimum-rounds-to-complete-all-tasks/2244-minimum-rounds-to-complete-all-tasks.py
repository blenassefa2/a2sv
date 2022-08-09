class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        count = defaultdict(int)
        
        for i in tasks:
            count[i] += 1
        

        rounds = 0
        for i in count:
            if count[i] == 1:
                return -1
            mod3 = count[i] % 3
            
            if mod3 == 0:
                rounds += count[i] // 3
            else:
                rounds +=( count[i] // 3)+ 1
        return rounds
                