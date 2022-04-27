class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count =  defaultdict(int)
        n = len(nums) / 2
        
        for i in nums:
            count[i] += 1
            if count[i] > n:
                return i