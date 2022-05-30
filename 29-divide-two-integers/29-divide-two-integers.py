class Solution:
    MAX_VALUE = 2**31 - 1
    MIN_VALUE = -(2**31)

    def divide(self, dividend: int, divisor: int) -> int:
        result = 0
        sign = 1 if dividend * divisor > 0 else -1
        current = abs(dividend)
        abs_divisor = abs(divisor)
        while abs_divisor <= current:
            i = 0
            while (abs_divisor << (i + 1)) <= current:
                i += 1
            current -= abs_divisor << i
            result += 2**i

        result *= sign
        result = max(self.MIN_VALUE, result)
        result = min(self.MAX_VALUE, result)
        return result