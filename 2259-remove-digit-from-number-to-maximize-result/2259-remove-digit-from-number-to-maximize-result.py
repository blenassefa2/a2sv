class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        """
        
        
        number = "312", digit = "3"
        
        iterate a pointer starting from least significant digit
        until I find the specfied digit
        
            I form new ans by concantating everyting before that index and everything after that index
        """
        
        
        lst = -1
        for i in range(len(number)):
            if number[i] == digit:
                lst = i
                if i+1<len(number) and number[i] < number[i + 1]:
                    return number[:i]+number[i+1:]
        return number[:lst]+number[min(lst+1, len(number)):]