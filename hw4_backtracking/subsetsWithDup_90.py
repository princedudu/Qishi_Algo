# Leetcode 90:
#
# https://leetcode.com/problems/subsets-ii/

# Runtime: 40 ms
# Memory Usage: 13.3 MB

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        nums.sort()
        stack = [[], [nums[0]]]
        pre = 1
        for i in range(1, len(nums)):
            start = pre if nums[i] == nums[i-1] else 0
            pre = len(stack)
            for j in range(start, len(stack)):
                stack.append(stack[j] + [nums[i]])
        return stack
