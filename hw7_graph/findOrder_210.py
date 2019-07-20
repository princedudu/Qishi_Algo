# Leetcode 210
#
# https://leetcode.com/problems/course-schedule-ii/


# Runtime: 108 ms
# Memory Usage: 15.2 MB

from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [[] for _ in range(numCourses)]
        outdegree = [0]*numCourses
        for course in prerequisites:
            indegree[course[0]].append(course[1])
            outdegree[course[1]] += 1

        ind0_dq = deque()
        for i in range(numCourses):
            if outdegree[i] == 0:
                ind0_dq.append(i)

        ind0_num = numCourses

        res = []
        while ind0_dq:
            ind0_v = ind0_dq.popleft()
            ind0_num -= 1
            res.append(ind0_v)
            for node in indegree[ind0_v]:
                outdegree[node] -= 1
                if outdegree[node] == 0:
                    ind0_dq.append(node)
        if ind0_num != 0:
            return []
        else:
            return res[::-1]
