class Solution:
    def reverseWords(self, s: str) -> str:
        lst = s.split(" ")
        
        ans = ""
        for i in range(len(lst)):
            ans += lst[i][::-1] + " "
        
        return ans[:-1]