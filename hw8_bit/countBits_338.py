# Leetcode 338:
#
# https://leetcode.com/problems/counting-bits/

# Runtime: 220 ms
# Memory Usage: N/A

class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num == 0:
            return [0]
        result = [0]
        for i in range(1, num+1):
            val = i
            count = 0
            while val:
                count += 1
                val = val & (val - 1)
            result.append(count)
        return result
