class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        [1,2,3,4,5,6,7]
        
        [7,6,5,4,3,2,1]
        
        5,6,7,1,2,3,4
        
        
        """
        k = k %len(nums)
        rest, first, count = 0, -1*k, 0
        
        ans = []
        
        while count < len(nums) and first:
            ans.append(nums[first])
            count += 1
            first += 1
        while count < len(nums):
            ans.append(nums[rest])
            count += 1
            rest += 1
        for i in range(len(ans)):
            nums[i] = ans[i]
            
#         right = k -1
#         left = len(nums) -1
#         while right>=0:
#             nums[right], nums[left] = nums[left], nums[right]
#             right -= 1
#             left -= 1
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #         t = len(nums) // 2
#         c = k % t
#         if k <= t:
#             right = k 
#             left = len(nums) -1
#             while right>1:
#                 nums[right], nums[left] = nums[left], nums[right]
#                 right -= 1
#                 left -= 1
#         else:
#             n = c + (k//t)+1
#             while n :
#                 right = t - 1
#                 left = len(nums) - 1
#                 while right:
#                     nums[right], nums[left] = nums[left], nums[right]
#                     right -= 1
#                     left -= 1
#                 n-=1
            
                
       
            
           
        