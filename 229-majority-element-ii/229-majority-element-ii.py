class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        
        
        n, ans = len(nums), set()
        if n < 3:
            return set(nums)
        winner = [nums[0], 1]
        
        for i in range(1,n):
            
            if winner[0] == nums[i]:
                winner[1] += 1
                if winner[1] > floor(n/3):
                    ans.add(winner[0])
            else:
                winner = [nums[i], 1]
        
        return ans
        