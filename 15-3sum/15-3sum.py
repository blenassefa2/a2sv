class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        i = 0
        while i < len(nums):
            key = nums[i] * -1
            l,r = i+1, len(nums) -1
            while l < r:
            
                s = nums[l] +nums[r]
                if s > key:
                    r -= 1 
                elif s < key:
                    l += 1
                elif s == key:
                    if r != i and l !=i and r != l:
                        a = min(nums[i],nums[r],nums[l])
                        c = max(nums[i],nums[r],nums[l])
                        b = sum([nums[i],nums[r],nums[l]]) - a- c
                        ans.add((a,b,c))
                    r -= 1
                    l += 1
            i += 1
                    
                    
        return list(ans)