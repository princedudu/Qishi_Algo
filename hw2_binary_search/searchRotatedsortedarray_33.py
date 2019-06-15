# Leetcode 33 Search in Rotated Sorted Array

# Binary search

# Runtime: 36 ms
# Memory Usage: 13.2 MB

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[end]:
                if target <= nums[mid] and target > nums[end]:
                    end = mid
                else:
                    start = mid
            else:
                if target <= nums[mid] or target > nums[end]:
                    end = mid
                else:
                    start = mid
            print([start, end])
        if nums[start] == target:
            return start
        elif nums[end] == target:
            return end
        else:
            return -1
