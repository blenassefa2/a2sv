class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = 0 
        
        c_array = [0]*(max(nums) + 1)
        
        for i in nums:
            c_array[i] += 1
        
        prefix = 0
        for j in range(len(c_array)):
            a = c_array[j] + prefix
            c_array[j] = prefix
            prefix = a
        
        ans = []
        for k in nums:
            ans.append(c_array[k])
        return (ans)
            
            
            