class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        two,t = 0 ,0
    
        for i in nums:
            two ^= i
            t ^= i
        k = 0
        while two:
            if not two&1:
                k += 1
                two >>= 1
                continue
            val = 0
            for i in range(len(nums)):
                
                if nums[i] &(1<<k):
                    val ^= nums[i]
            return [val,t^val] 