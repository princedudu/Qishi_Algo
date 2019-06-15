# Leetcode 74 Search a 2D Matrix

# Binary search

# Runtime: 32 ms
# Memory Usage: 14 MB

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        start, end = 0, m-1
        if matrix[0][0] > target or matrix[-1][-1] < target:
            return False
        while start <= end:
            mid = start + (end - start) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                if mid == m - 1 or matrix[mid+1][0] > target:
                    sel = mid
                    break
                else:
                    start = mid + 1
            else:
                end = mid - 1

        for j in range(n):
            if matrix[sel][j] == target:
                return True
        return False

# Linear search

# Runtime: 36 ms
# Memory Usage: 13.9 MB

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        i, j = m - 1, 0
        while i >= 0 and j <= n - 1:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                j += 1
            else:
                i -= 1
        return False
