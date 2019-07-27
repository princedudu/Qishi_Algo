# Leetcode 190:
#
# https://leetcode.com/problems/reverse-bits/

Runtime: 24 ms
Memory Usage: N/A

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        m = 32
        res = 0
        while m > 0:
            res = (res << 1) + (n & 1)
            n = n >> 1
            m -= 1
        return res
