# Runtime: 44 ms
# Memory Usage: 13.4 MB


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        current = current_max = nums[0]
        for i in range(1, len(nums)):
            if current < 0:
                current = nums[i]
            else:
                current += nums[i]
            res = max(res, current)
        return res
