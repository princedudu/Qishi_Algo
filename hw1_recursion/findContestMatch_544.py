# 544.  Output Contest Matches

class Solution:
    """
    @param n: a integer, denote the number of teams
    @return: a string
    """
    def findContestMatch(self, n):
        # write your code here
        if n % 2:
            return False
        s = [str(i) for i in range(1, n + 1)]

        while n > 1:
            for i in range(n/2):
                s[i] = '(' + s[i] + ',' + s[n-1-i] + ')'

            n = n / 2
        return s[0]
