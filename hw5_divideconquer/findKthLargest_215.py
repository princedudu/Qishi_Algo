# Runtime: 32 ms
# Memory Usage: 13.6 MB

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if k == len(nums):
            return min(nums)
        if k == 1:
            return max(nums)
        pivot = nums[0]
        left = [x for x in nums if x > pivot]
        right = [x for x in nums if x < pivot]
        middle = [x for x in nums if x == pivot]
        if k <= len(left):
            return self.findKthLargest(left, k)
        if len(left) < k <= len(left) + len(middle):
            return pivot
        return self.findKthLargest(right, k - len(left) - len(middle))
