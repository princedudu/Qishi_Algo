# Leetcode 40:
#
# https://leetcode.com/problems/combination-sum-ii/


# Runtime: 100 ms
# Memory Usage: 13.3 MB


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        self.dfs(candidates, [], res, target)
        return res

    def dfs(self, candidates, current, res, target):
        if target == 0:
            res.append(current)
        i = 0
        while i < len(candidates):
            if candidates[i] <= target:
                self.dfs(candidates[i+1:], current + [candidates[i]], res, target - candidates[i])
            while i+1 < len(candidates) and candidates[i+1] == candidates[i]:
                i += 1
            i += 1
