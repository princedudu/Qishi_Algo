# Leetcode 47:
#
# https://leetcode.com/problems/permutations-ii/


# Runtime: 72 ms
# Memory Usage: 13.5 MB


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        nums.sort()
        res = []
        self.backtracking(nums, [], res)
        return res

    def backtracking(self, nums, current, res):
        if not nums:
            res.append(current)
        i = 0
        while i < len(nums):
            self.backtracking(nums[:i] + nums[i+1:], current + [nums[i]], res)
            while i + 1 < len(nums) and nums[i] == nums[i +1]:
                i += 1
            i += 1
