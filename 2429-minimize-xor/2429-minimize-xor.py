class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        """
        first I count the number of ones I have on nums2
        
        then starting from the most significant bit I start to assign 1 to 1s and 0 to the zeros
        
        if I finish my ones before finishing nums1 I fill the rest with 0
        
        """
        
        ones = (list(bin(num2)[2:])).count("1")
        num1 =  list('{:032b}'.format(num1))
        
        for i in range(len(num1)):
            if num1[i] == "1":
                ones -=1
                if ones == 0:
                    for j in range(i+1, len(num1)):
                        num1[j] = "0"
                    return int("".join(num1),2)
        for k in range(len(num1)-1, -1, -1):
            if num1[k] == "0":
                num1[k] = "1"
                ones -=1
            if ones <= 0:
                return int("".join(num1),2)
       