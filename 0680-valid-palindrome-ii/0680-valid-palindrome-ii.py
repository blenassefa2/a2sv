class Solution:
    def checkPali(self, l,r, s):
        while l < r:
            if s[l] != s[r]:
                 return False
            l += 1
            r -= 1
        return True
    def validPalindrome(self, s: str) -> bool:
        """
        There are Three scenarios:
        1. no delete needed
            if s is already palindrome
        2. delete one char
            while checking if s is palindrome and we face a point where the chars are not similar
           2.1
            then we will try to continue checking not minding the left
            then we will try to continue checking not minding the right
            
            if one of the two ways work then that means we can remove one of them
            
        3. it is impossible
            
            after performing 2.1 if both ways don't work
            
        """
        
        # initialize variables
        removeL = []
        removeR = []
        isPali = True
        left = 0
        right = len(s) -1
        
        
        # continue with checking if s is palindrome
        while left < right:
            
            while left < right and s[left] == s[right]:
                left += 1
                right -= 1
                
            if left < right and s[left] != s[right]:
                removeL = [left + 1, right]
                removeR = [left, right-1]
                isPali = False
                break
      
        if isPali == False:
            opt1 = self.checkPali(removeL[0], removeL[1], s)
            opt2 = self.checkPali(removeR[0], removeR[1], s)
          
            isPali = opt1 or opt2
       
        return isPali
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        