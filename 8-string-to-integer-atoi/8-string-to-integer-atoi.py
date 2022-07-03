class Solution:
    def myAtoi(self, s: str) -> int:
        ans = 0
        i = 0
        sign = 1
        nums = deque([])
        while i < len(s) and s[i] == ' ':
            i += 1
        if i >= len(s):
            return ans
        if "0" > s[i] or s[i] > "9":
           
            if s[i] == '-':
                sign = -1
            elif s[i] !='+':
                return ans
            i += 1
        while i < len(s) and "0" <= s[i] <= "9":
            nums.append(s[i])
            i += 1
        
        mult = 10 ** (len(nums) - 1)
        while nums:
            a = int(nums.popleft()) * mult
            ans += a
            mult //= 10
            
        if sign == -1:
            return max(ans*-1, -1 * (2**31))
        return min((2**31) - 1, ans)
                