class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        def magic(LB,RB, win_size):
           
            l,r,sum_ = 0,0,0
            final = 0
            for i in range(win_size):
                sum_ += nums[r]
                r += 1
            
            while r < len(nums):
                if (r<LB<=RB or LB<=RB<l):
                    final = max(final, sum_)
                
                sum_ += nums[r] 
                sum_ -= nums[l] 
                
                l += 1     
                r += 1
                
            if (r<LB<=RB or LB<=RB<l):
                final = max(final, sum_)
                
            return final
        
        lt,rt,s = 0,0,0
        f = 0
        for i in range(firstLen):
            s += nums[rt]
            rt += 1

        while rt < len(nums):
            
            f = max(f, s + magic(lt,rt-1,secondLen))

            s += nums[rt] 
            s -= nums[lt] 

            lt += 1     
            rt += 1
        return max(f, s + magic(lt,rt,secondLen))