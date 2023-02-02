class Solution:
    def numberOfWays(self, s: str) -> int:
        """
        the question asks to find how many 101 and 010 subsequences are there
        
        so we can check for every index what if it is the middle value
        thus I will keep track of number of 0's and number of ones
        then calculate number of zeros before and after each index
        
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        
        onesR = 0
        zerosR = 0
        
        for i in s:
            onesR += int(i)
        zerosR = len(s) - onesR
        onesL = 0
        zerosL = 0
        
        total = 0
        for i in range(len(s)):
            if s[i] == "0":
                total += (onesL * onesR)
                zerosL += 1
                zerosR -= 1
            else:
                total += (zerosL * zerosR)
                onesL += 1
                onesR -= 1
        
        return total
        
        