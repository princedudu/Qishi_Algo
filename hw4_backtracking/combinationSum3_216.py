# Leetcode 216:
#
# https://leetcode.com/problems/combination-sum-iii/

# Runtime: 40 ms
# Memory Usage: 13.3 MB

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(range(1,10), 0, [], k, n, res)
        return res

    def dfs(self, nums, idx, items, k, target, res):
        if len(items) == k:
            if sum(items) == target:
                res.append(items[:])
            return

        if len(items) > k:
            return

        if sum(items) >= target:
            return

        for i in range(idx,len(nums)):
            items.append(nums[i])
            self.dfs(nums, i + 1, items, k, target, res)
            items.pop()
