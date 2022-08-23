class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        score= 0
        while(target > 1):
            if maxDoubles and not target%2:
                target = target // 2
                maxDoubles -= 1
            else:
                target -= 1
            if not maxDoubles:
                score += target
                break
            score += 1
        return score