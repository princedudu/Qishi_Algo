# 200. Number of Islands

# Runtime: 76 ms
# Memory Usage: 13.8 MB

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j, m, n)
                    res += 1
        return res
        

    def dfs(self, grid, i, j, m, n):
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == '0':
            return
        else:
            grid[i][j] = '0'
            self.dfs(grid, i-1, j, m, n)
            self.dfs(grid, i+1, j, m, n)
            self.dfs(grid, i, j-1, m, n)
            self.dfs(grid, i, j+1, m, n)
