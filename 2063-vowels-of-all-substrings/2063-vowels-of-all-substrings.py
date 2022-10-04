class Solution:
    def countVowels(self, word: str) -> int:
        a, b, c = [1], [], []
        
        
        for i in word:
            if i in {'a','e','i','o','u'}:
                a.append(1)
            else:
                a[-1] += 1
        for i in range(len(a)):
            b.append(a[i])
            c.append(i*a[i])
            if i != 0:
                b[-1] += b[-2]
                c[-1] += c[-2]    
        ans = 0
        
        for i in range(len(a)):
            ans += a[i]*((i*b[i]) -c[i])
        return ans
            
                    