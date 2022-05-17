class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        all_ = 0
        s = list(set(nums))
        nw = 0
        original = 0
        
        for x in nums:
            original ^= x
            
        for i in range(len(nums)+1):
            all_ ^=i
        
        for j in s:
            nw ^= j
        return [nw^original, all_^ nw] 
            