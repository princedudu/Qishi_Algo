# Leetcode 278 First Bad Version

# Binary search

# Runtime: 36 ms
# Memory Usage: 13.2 MB

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start, end = 1, n
        while start + 1 < end:
            mid = start + (end - start) // 2
            if isBadVersion(mid):
                end = mid
            else:
                start = mid
        if isBadVersion(start):
            return start
        if isBadVersion(end):
            return end
