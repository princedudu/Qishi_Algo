# Leetcode 77:
#
# https://leetcode.com/problems/combinations/

# Runtime: 560 ms

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k == 0 or n == 0:
            return []
        res = []
        self.dfs([i for i in range(1, n + 1)], k, [], res)
        return res

    def dfs(self, candidate, k, current, res):
        if k == 0:
            res.append(current)
            return
        if not candidate:
            return
        for i, item in enumerate(candidate):
            self.dfs(candidate[i+1:], k - 1, current + [item], res)
