class Solution:
    
    def countGoodNumbers(self, n: int) -> int:
        if n == 1:
            return 5
        
        a = (n//2)
        b = a +(1*(n%2))
        mod = pow(10,9) + 7
        return (pow(4, a, mod) * pow(5, b, mod))  %(1000000007)
   
       
    """
    1: 5        2:20        4
    2: 20       4:400       20
    3: 100      6:8000      80
    4: 400      8: 160000   400
    
    
    
    """