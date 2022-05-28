class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        ind = set()
        
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                l, r = j + 1, len(nums) - 1
                t =  target - (nums[i] + nums[j])
                while l < r:
                    
                    s = nums[l] + nums[r]
                    
                    if s > t:
                        r -= 1
                    elif t > s:
                        l += 1
                    elif t == s:
                        if (nums[i], nums[j], nums[l], nums[r]) not in ind:
                            ans.append([nums[i], nums[j], nums[l], nums[r]])
                            ind.add((nums[i], nums[j], nums[l], nums[r]))
                        l += 1
                        r -= 1
        return ans