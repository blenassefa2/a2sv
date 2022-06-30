class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        prefix= [0]
        
        for i in range(len(nums)):
            if prefix[-1] < 0:
                prefix.append(nums[i])
            else:
                prefix.append(nums[i] + prefix[-1])
        return(max(prefix[1:]))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         total = sum(nums)
#         final = total
#         l,r = 0,len(nums) -1
        
#         while l <= r:
#             if nums[l] > nums[r]:
#                 total -= nums[r]
#                 r -= 1
                
#             elif nums[l] < nums[r]:
#                 total -= nums[l]
#                 l += 1
#             elif nums[l] == nums[r]:
#                 total -= nums[l]
                
#                 if l < len(nums)-1 and r>0 and nums[l+1] >nums[r-1]:
#                     r -= 1
#                 else:
#                     l +=1
                
#             if total > final:
#                 final = total
#         return (final)
        
        