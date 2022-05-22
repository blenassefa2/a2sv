class Solution:
    def longestPalindrome(self, s: str) -> str:
        def paliLen(a,b):
            
            while a >= 0 and b < len(s) and s[a] == s[b]:
                
                a -= 1
                b += 1
                
            return a+1,b-1
        
        ans = 0,0
        for i in range(len(s)):
            ans = max(ans,paliLen(i,i),paliLen(i,i+1), key=lambda b: b[1] - b[0])
        return s[ans[0]:ans[1] + 1]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #         ans = ""
#         print(len(s))
#         for i in range(len(s)):
#             for j in range(i+1,len(s)):
#                 a = s[i:j+1]
#                 if (a == (a)[::-1]):
#                     ans = max(ans,a, key = lambda x:len(x))
#                     break
#         return ans
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         visited = set()
#         def cross(l,r,m):
#             c = 0
#             while l <= r:
#                 if s[l] == s[l]:
#                     l += 1
#                     r -= 1
#                     c += 1
#                 else:
#                     c = 0
#                     l += 1
#                     r -= 1
                
#             return (l-c,r+c)
        
#         def greedy(l,r):
#             if r == l:
#                 return (l,r)

#             m = (l+r) //2

#             left =  greedy(l,m)
#             middle = cross(l,r,m)
#             right = greedy(m+1,r)

#             print("left = ", left,"right = ",right,"middle = ",middle)
#             return max(left,middle,right, key = lambda x: x[1] - x[0])
                
              
                
      
#         ans  = greedy(0,len(s)-1)
#         return s[ans[0]:ans[1]+1]
        
            
            