class Solution:
    def secondHighest(self, s: str) -> int:
       
        largest, second_l = -1, -1
        s = list(s)
        s.sort()
        s= "".join(s)
        print(s)
        p = 0
        
        while p < len(s):
            if  s[p].isnumeric():
                if int(s[p]) > largest:
                    second_l = largest
                    largest = int(s[p])
            
            p += 1
        return second_l
                    