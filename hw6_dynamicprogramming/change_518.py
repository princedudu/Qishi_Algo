# Leetcode 518 Coin Change 2

# Runtime: 148 ms
# Memory Usage: 13.5 MB

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for j in range(coin, amount+1):
                dp[j] += dp[j -coin]
        return dp[-1]
