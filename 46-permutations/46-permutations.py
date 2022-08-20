class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        ans = set()
        def recurs(i, arr):
            if i == len(nums) - 1:
                return
            
           
            
            for j in range(len(nums)):
                new = [n for n in arr]
                new[j], new[i] = new[i], new[j]
                ans.add(tuple(new))
                recurs(i+1, new)
        recurs(0,nums)
        return (ans)