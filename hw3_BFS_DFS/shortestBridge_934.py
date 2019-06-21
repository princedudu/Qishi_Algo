# 934. Shortest Bridge

# Runtime: 172 ms
# Memory Usage: 16.7 MB

class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:


        def dfs(i, j):
            A[i][j] = -1
            bfs.append((i, j))
            for k, l in ((i - 1, j), (i+1, j), (i, j-1), (i, j+1)):
                if 0<=k < m and 0<=l < n and A[k][l] == 1:
                    dfs(k, l)

        def find(A):
            for i in range(m):
                for j in range(n):
                    if A[i][j]:
                        return (i, j)

                # print(i, j)

        m, n = len(A), len(A[0])
        step = 0
        bfs = []

        (i_s, j_s) = find(A)
        dfs(i_s, j_s)

        while bfs:
            tmp = []
            for i, j in bfs:
                for k, l in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                    if 0 <= k < m and 0 <= l < n:
                        if A[k][l] == 1:
                            return step
                        elif not A[k][l]:
                            A[k][l] = -1
                            tmp.append((k, l))
            bfs = tmp
            step += 1
