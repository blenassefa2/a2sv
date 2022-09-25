class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        s = defaultdict(int)
        for i in range(len(nums)):
            s[target - nums[i]] = i
       
        for i in range(len(nums)):
            if nums[i] in s and i != s[nums[i]]:
                return [i, s[nums[i]]]