# 542. 01 Matrix

# Runtime: 536 ms
# Memory Usage: 15.5 MB

import sys

class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        bfs = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] != 0:
                    matrix[i][j] = sys.maxsize
                else:
                    bfs.append((i, j))

        for (i, j) in bfs:
            for k, l in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                tmp = matrix[i][j] + 1
                if 0 <= k < m and 0 <= l < n and matrix[k][l] > tmp:
                    matrix[k][l] = tmp
                    bfs.append((k, l))
        return matrix
