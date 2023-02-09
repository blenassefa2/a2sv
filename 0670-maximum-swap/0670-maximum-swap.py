class Solution:
    def maximumSwap(self, num: int) -> int:
        """
        for this question there is either a swap or not
        
        
        ''
        
        """
        digits = list(str(num))
        
        
        for i in range(len(digits)):
            m = i
            for j in range(i + 1, len(digits)):
                if digits[m] <= digits[j]:
                    m = j
            if digits[m] != digits[i]:
                digits[i], digits[m] = digits[m], digits[i]
                return int("".join(digits))
            
        return num