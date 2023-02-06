ones_ = ["","One ","Two ","Three ", "Four ", "Five ", "Six ", "Seven ", "Eight ", "Nine "]
twos_ = ["","", "Twenty ","Thirty ","Forty ","Fifty ","Sixty ","Seventy ","Eighty ", "Ninety "]
ten_ = ["Ten ","Eleven ","Twelve ","Thirteen ","Fourteen ","Fifteen ","Sixteen ","Seventeen ","Eighteen ","Nineteen "]
lables = ["", "", "Thousand ", "Million "]

def recurs(n, s):
    if n == 0:
        return s
    length = floor(log10(n)) +1

    if length == 1:
        s += ones_[n]
        return s
    if length == 2:
        k = n // 10
        if k == 1:
            s += ten_[n % 10]
            return s

        s += twos_[k]
        if n%10 == 0:
            return s
        return recurs(n%10, s)
    if length == 3 or length == 6 or length == 9:
        s  += ones_[n // pow(10,(length - 1))] + "Hundred "
        k = n% pow(10,(length - 1))
        if k == 0 or floor(log10(k)) +1 < length - 2:
            s += lables[length // 3]
        return recurs(k, s)

    if length == 7:
        k = n // 1000000
        s += ones_[k] + "Million "
        return recurs(n % 1000000, s)

    if length == 8:
        k = n // 10000000
        if k == 1:
            s += ten_[(n // 1000000) - 10] + "Million "
            return recurs(n % 1000000, s)
        s += twos_[k]
        if n%10000000 == 0 or floor(log10(n%10000000)) +1 < 7:
            s += "Million "
        return recurs(n%10000000, s)

    if length == 4:
        k = n // 1000
        s += ones_[k] + "Thousand "
        return recurs(n % 1000, s)

    if length == 5:
        k = n // 10000
        if k == 1:
            s += ten_[(n // 1000) - 10] + "Thousand "
            return recurs(n % 1000, s)
        s += twos_[k]
        if n%10000 == 0 or floor(log10(n%10000)) +1 < 4:
            s += "Thousand "
        return recurs(n%10000, s)

    if  length == 10:
        s += ones_[n // 1000000000] + "Billion "
        return recurs(n %1000000000, s)   
class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        answer = recurs(num,"")[:-1]
        return answer
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         ans = ""
        
#         t = 0 
                                                            
        
#         while True: 
#             if t == len(s):
#                 break
    
            
#             y = len(s) - t
#             index = (len(s) - t)% 3
            
#             if index == 2:
#                 if s[t] == "1":
#                     ans += ten_[int(s[t +1])] + lables[y // 3]
#                     t +=1
#                 else:
#                     ans += twos_[int(s[t])]+ lables[y // 3]
#                     t +=1
#             else:
                
                
                
#                 if index == 0:
#                     if s[t] != "0":
#                         ans += ones_[int(s[t])] + "Hundred "
#                         if s[t+1] =="0" and s[t+2] == "0":
#                             x =(len(s) -(t+2)) //3 
#                             ans += lables[x]
#                 else:
#                     if s[t] != "0":
#                         ans += ones_[int(s[t])] + lables[y // 3]
           
#             t+=1
        
        
        
        
        # while true 
            #if t == len(s) break
            
    
            # to handle just the numbers
            # y = len(s) - t
            # index = (len(s) - t)% 3
            # if index is 2
                # if s[t] == "1"
                    # append ans from ten_ 
                # else
                    # append ans from twos_ 
            # if index is 0 or 1
                # if index is 0
                    # append ans from ones_ +"hundreds"
                # else
                    # append ans from ones_ + lables[y // 3]
                        
                
        # return ans[:-1]
    
    
    """
    
    
    class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        nums = [-1 *((x%2 ) -1)for x in nums]
        right = 0
        left = 0
        max_ = []
        count = k
        while right < len(nums) :
            
            while right < len(nums) and (nums[right] or k):
                k -= abs(nums[right] - 1)
                right += 1
              
            max_.append(right - left) 
            if k < count:
                 k += abs(nums[left] - 1)      
            left += 1
            if left >= right:
                right = left
                
        return len(max_)
    class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        nw = [1 - (i%2) for i in nums]
        
        right = 0
        left = 0
        counter = 0
        odds= 0
        while right < len(nw) :
            
            
            while right < len(nw) and (nw[right] or k):
                
                odds += (1 - nw[right])
                right += 1
                if odds == k:
                    counter+=2
                    break
       
                
            while left < right and odds == k:
                left +=1
                odds -= (1 - nw[left])
                counter += 2
            
            while right <len(nw) and nw[right]:
                right += 1
                counter += 2
            left += 1
        
        
        if 0 in nw:      
            return (counter)
        return 0    
        
    """
    