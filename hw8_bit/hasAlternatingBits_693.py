# Leetcode 693:
#
# https://leetcode.com/problems/binary-number-with-alternating-bits/

# Runtime: 36 ms
# Memory Usage: N/A

class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        pre = n & 1
        while n > 0:
            n = n >> 1
            curr = n & 1
            if pre == curr:
                return False
            pre = curr
        return True
