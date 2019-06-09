#leetcode 247. Strobogrammatic Number II

#performance (leetcode not available)


class Solution:
    """
    @param n: the length of strobogrammatic number
    @return: All strobogrammatic numbers
    """

    def __init__(self):
       self.one_digit = ['0', '1', '8']
       self.two_digit = ['11', '69', '88', '96', '00']

    def findStrobogrammatic(self, n):
        if n == 0:
            return [""]
        elif n == 1:
            return self.one_digit
        elif n == 2:
            return self.two_digit[:-1]

        res = []
        if n % 2 == 0:
            side, mid = self.findStrobogrammatic(n - 2), self.two_digit
        else:
            side, mid = self.findStrobogrammatic(n - 1), self.one_digit

        for s in side:
            for m in mid:
                res.append(s[:(n-1)//2] + m + s[(n-1)//2:])
        return res
