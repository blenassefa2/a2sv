class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        
        n, ans = len(nums), set()
    
        winner = [None, None]
        w_count = [0,0]
        
        for i in range(n):
            
            if nums[i] == winner[0]:
                w_count[0] += 1
            elif nums[i] == winner[1]:
                w_count[1] += 1
            elif not w_count[0]:
                winner[0] = nums[i]
                w_count[0] += 1
            elif not w_count[1]:
                winner[1] = nums[i]
                w_count[1] += 1
            else:
                w_count[0] -= 1
                w_count[1] -= 1
        
        if nums.count(winner[0]) > floor(n/3):
            ans.add(winner[0])
        if nums.count(winner[1]) > floor(n/3):
            ans.add(winner[1])
       
            
        return ans
        