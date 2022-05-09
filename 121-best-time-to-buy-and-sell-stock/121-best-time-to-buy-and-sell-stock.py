class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices) ==1:
            return 0
        if len(prices) == 2:
            return max(0,prices[1] -prices[0])
                
        
        
        buy = prices[0]
        sell = prices[1]
        
        max_ = sell - buy
        
        for i in range(2,len(prices)):
            
            x = min(buy,sell)
            
            
            if max_ < prices[i] -x:
                sell = prices[i]
                buy = x
                max_ = sell - buy
            if buy > prices[i]:
                buy = prices[i]
        return max(0,max_)