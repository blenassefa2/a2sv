class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        """
        Find the factors of a and put it in a set:
        find the factors of b and when ever you find it in the previously stored set count it
        
        Time complexity O(a+b)
        space complexity O(a)
        """
        
        setA = set()
        for i in range(1,a+1):
            if not a%i:
                setA.add(i)
                
        count = 0
        for j in range(1,b+1):
            if not b%j:
                if j in setA:
                    count += 1
                
        return count