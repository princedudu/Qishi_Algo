# Runtime: 68 ms
# Memory Usage: 13.2 MB

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        length1 = len(nums1)
        length2 = len(nums2)
        k = (length1 + length2) // 2
        if (length1 + length2) % 2 == 0:
            return (self.find(nums1, nums2, k) + self.find(nums1, nums2, k-1)) / 2
        else:
            return self.find(nums1, nums2, k)

    def find(self, nums1, nums2, k):
        if not nums1:
            return nums2[k]
        if not nums2:
            return nums1[k]
        if k == 0:
            return min(nums1[0], nums2[0])

        length1 = len(nums1)
        length2 = len(nums2)
        if nums1[length1//2] > nums2[length2//2]:
            if k > length1//2 + length2//2:
                return self.find(nums1, nums2[length2//2+1:], k - length2//2 -1)
            else:
                return self.find(nums1[:length1//2], nums2, k)
        else:
            if k > length1//2 + length2//2:
                return self.find(nums1[length1//2+1:], nums2, k - length1//2-1)
            else:
                return self.find(nums1, nums2[:length2//2], k)
