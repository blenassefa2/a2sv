class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l,r = 0,0
       
        
        while r < len(nums):
           
            if 0<l and nums[l] < nums[l-1]:
                break
            while r< len(nums) and nums[r] == nums[l]:
                # if nums[r] 
                r += 1
            
            

            count = 0
            while l+1 < len(nums) and nums[l] ==nums[l+1] and count < 2:
                count += 1
                l += 1
            
            if count <2:
                l +=1
                continue
             
            if r < len(nums):    
                if nums[l] > nums[r]:
                    break
                nums[l], nums[r] = nums[r], nums[l]
                temp =l + 1
                r += 1
                while r < len(nums) and nums[temp] < nums[r]:
                    nums[temp], nums[r] = nums[r], nums[temp]
                    r += 1
                    temp += 1
               
                r = l
        
        return l