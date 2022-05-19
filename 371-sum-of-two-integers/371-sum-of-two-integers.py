class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        def add(a,b):
            sum_, carry = 0,1
            
            while carry:
                sum_, carry = a^b, ((a&b) <<1)
                a,b = sum_, carry
            return sum_
          
        def sub(a,b):
            big = 1<<(len(bin(a)) - 2)
            sm = int("1"*(len(bin(a)) - 2),2)
           
            y = sm ^ b
            
           
            x = add(a,y)
            x = add(x, 1)
           
            
            
            return big^x
        if a >= 0 and b >=0:
            return add(a,b)
        if a <0 and b <0:
            return -1 * add(abs(a),abs(b))
        x = max(abs(a),abs(b))
        y = min(abs(a),abs(b))
        
        
        ans = sub(x,y)
        if (abs(a) >= abs(b) and a >= b) or (abs(b) >= abs(a) and b >= a) :
            return ans
        return -1*ans