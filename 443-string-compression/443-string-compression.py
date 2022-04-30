class Solution:
    def compress(self, chars: List[str]) -> int:
            
        nums = deque()
        x = chars[0]
        count = 1
        
        for i in range(1,len(chars)):
            if chars[i] == x:
                count += 1
                chars[i] = ""
            else:
                if count > 1:
                    nums.append(count)
                count = 1
                x = chars[i]
        if count > 1:
            nums.append(count)
        j = 1
        
        while j < (len(chars)):
            
            if chars[j] == "":
                if not nums:
                    break
                y = nums.popleft()
               
                for v in str(y):
                    chars[j] = v
                    j += 1
                a,b = j,j
                while a < len(chars) and chars[a] == "":
                    a+= 1
                while a <len(chars):
                    chars[b] = chars[a]
                    a+=1
                    b+=1
                while b <len(chars):
                    chars[b] = ""
                    b += 1
                if j <len(chars) and chars[j] =="":
                    break
            
            j+=1
        
        return j
        
                
                
                
        
        
        
        
