class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = [amount+1] * (amount + 1)
        cache[0] = 0
        
        for i in range(1,amount+1):
            for coin in coins:
                if i - coin >= 0:
                    cache[i] = min(cache[i], 1 + cache[i - coin])
        
        return cache[amount] if cache[amount] != amount + 1 else -1