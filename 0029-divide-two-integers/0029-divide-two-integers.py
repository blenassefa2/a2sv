class Solution:
    def dividePositive(self,dividend,divisor,sign):
        
        
        quotient = 0
        
        # perform bit division
        while dividend >= divisor:
            
            newDivisor = 0
            while divisor << (newDivisor+1) <= dividend:
                newDivisor += 1
                
            dividend -= (divisor << newDivisor)
            quotient |= (1<<newDivisor)
            
        
        return quotient
            
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend*divisor < 0:
            return max(-2147483648, -self.dividePositive(abs(dividend),abs(divisor), -1))
        else:
            return min(2147483647, self.dividePositive(abs(dividend),abs(divisor),1 ))
        