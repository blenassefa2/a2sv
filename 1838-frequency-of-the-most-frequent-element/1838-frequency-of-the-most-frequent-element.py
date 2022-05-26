class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l,r = 0,0
        currTotal = 0
        ans = -1
        while r < len(nums):
            
            while (nums[r]*(r-l))-currTotal > k:
                
                currTotal -= nums[l]
                l += 1
            ans = max(ans,(r -l+1))
            currTotal += nums[r]
            r += 1
                    
            
        return(ans)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         """
#         best =2
#          0 1 2 3 4 5   6  7    8  9   10 
#         [1,4,8,8,8,13,100,200,300,400,500] k = 5
#                     |      |             |
#         """
#         count = defaultdict(int)
        
       
#         visited =  set()
#         nums.sort()
        
#         for i in nums:
#             count[i] += 1
            
            
#         def magic(a):
#             if nums[a] not in visited:
#                 visited.add(nums[a])
#                 n, b = 0, a - 1
                
#                 while b >= 0:
#                     if (nums[a] - nums[b]) <= (k - n):
#                         n += (nums[a] - nums[b])
#                         count[nums[a]] += 1
#                     b -= 1
#             return count[nums[a]]
            
            
    
#         left, right, best = 0, len(nums) - 1, 1
        
        
#         while left <= right:
#             mid = (left + right) //2
            
#             x = magic(mid)
            
#             if best > x:
#                 right = mid - 1
            
        
#         return (maxf)
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# #         nums.sort()
# #         prefix_sum = [0]
# #         for i in range(len(nums)-1):
# #             prefix_sum.append(prefix_sum[-1] +(nums[i+1] - nums[i]))
        
# #         left= 1
# #         right = len(nums) 
# #         while left <= right:
# #             mid = (left+right)//2
# #             sum_ = 0
# #             if mid <len(nums):
# #                 s =  nums.count(nums[mid]) 
            
# #             for i in range(s-1,mid):
# #                 sum_ += (prefix_sum[mid-1] - prefix_sum[i])
           
# #             if sum_ <= k :
# #                 best = mid
# #                 left = mid +1
# #             else:
# #                 right = mid -1
                       
# #         return best
        
                       
                       
#         """
#         [1,2,4]
#           1 2
#         0 1 3
         
#         1 < ans < len(nums) 
#         move left and save best if we can have "mid" frequency
#         sum_ = 0
#         for i in range(mid-1)
#             sum_ += (prefix_sum[mid-1] - prefix_sum[i])
            
#          1, 2, 3
#                |
#                   |
#                |
        
        
#         """