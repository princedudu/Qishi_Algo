# Leetcode 64 Minimum Path Sum

# Runtime: 48 ms
# Memory Usage: 13.5 MB

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        dp = grid[0]
        for j in range(1, n):
            dp[j] += dp[j-1]
        for i in range(1, m):
            dp[0] += grid[i][0]
            for j in range(1, n):
                dp[j] = min(dp[j-1], dp[j]) + grid[i][j]
        return dp[-1]
