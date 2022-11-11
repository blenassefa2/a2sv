class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        valid = lambda a,b,c: nums[a]+nums[b] > nums[c]
        
        nums.sort()
        sumUp = lambda a,b,c: nums[a] + nums[b] + nums[c]
        z = len(nums) - 1
        y = z - 1
        x = y - 1
        while x >= 0:
        
            if valid(z,y,x) and valid(y,x,z) and valid(x,z,y):
                
                return sumUp(x,y,z)
            z -= 1
            x -= 1
            y -= 1
        return 0