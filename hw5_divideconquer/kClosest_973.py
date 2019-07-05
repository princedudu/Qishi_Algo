# Runtime: 408 ms
# Memory Usage: 27.2 MB


class Solution:
    import math
    def kClosest(self, points: List[List[int]], K: int):
        def dist(p):
            p1, p2 = p
            return math.sqrt(p1**2 + p2**2)

        distances = [(dist(p), p) for p in points]


        def partition(left, right, pivot_index):
            nonlocal distances
            pivot = distances[pivot_index]
            distances[pivot_index], distances[right] = distances[right], distances[pivot_index]
            stored_index = left
            for i in range(left, right):
                if distances[i][0] <= pivot[0]:
                    distances[i], distances[stored_index] = distances[stored_index], distances[i]
                    stored_index += 1
            distances[stored_index], distances[right] = distances[right], distances[stored_index]
            return stored_index

        def select(left, right, k):
            if left >= right: return left
            pivot_index = random.randint(left, right)
            pivot_index = partition(left, right, pivot_index)
            print("curr:", pivot_index)
            if pivot_index == k:
                return pivot_index
            elif pivot_index > k:
                return select(left, pivot_index-1, k)
            else:
                return select(pivot_index + 1, right, k)

        idx = select(0, len(distances) - 1, K)
        res = [distances[i][1] for i in range(idx)]
        return res
