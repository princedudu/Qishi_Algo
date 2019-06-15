# Leetcode 69 Sqrt(x)



# Binary search method
# Runtime: 52 ms
# Memory Usage: 13.3 MB
class Solution:
    def mySqrt(self, x: int) -> int:
        start, end = 0, x
        mid = end
        while abs(mid * mid - x) > 1e-2:
            if mid * mid < x:
                start = mid
            else:
                end = mid
            mid = start + (end - start) / 2
        return int(mid)


# Newton method
# Runtime: 32 ms
# Memory Usage: 13.1 MB
class Solution:
    def mySqrt(self, x: int) -> int:
        y = x
        while abs(y * y - x) > 1e-3:
            y = y/2 + x/2/y
        return int(y)
