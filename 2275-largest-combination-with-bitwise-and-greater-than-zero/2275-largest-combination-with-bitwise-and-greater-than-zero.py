class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        length = floor(log2(max(candidates)))
        mask = 1
        mask<<= length 
        ans = -10000000
        


        while length >= 0:
            count = 0
            # print(bin(mask))
            for a in candidates:

                if a&mask:
                    count +=  1
            ans = max(ans,count)
            mask>>=1
            length -= 1
            
        return(ans)