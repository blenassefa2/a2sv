class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        l = area
        w = 1
        
        answer = [l,w]
        while w <= l:
            
        
            if l == int(l):
                answer = min(answer, [int(l),w], key=lambda x: x[0] - x[1] )
            w += 1
            l = area / w
        return answer