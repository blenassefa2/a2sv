class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @lru_cache(maxsize= None)
        def dp(status, index):
            if index >= len(prices):
                return 0
            
            if status == 1: # we can buy or jump
                notJump = dp(0, index + 1) - prices[index]
            else:
                notJump = dp(1, index + 2) + prices[index]
            
            jump = dp(status, index + 1)
            return max(jump, notJump)
        
        return dp(1, 0)
                
                
                