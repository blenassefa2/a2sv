class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]
        for i in range(len(nums)):
            pre.append(pre[-1]*nums[i])
        nums.append(1)
        for i in range(len(nums)-2, -1, -1):
            nums[i] = nums[i] *nums[i+1]
        
        
    
        for i in range(1, len(nums)):
            nums[i] = nums[i] *pre[i-1]
        return nums[1:]
            
            