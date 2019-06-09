# 698. Partition to K Equal Sum Subsets

class Solution:
    def canPartitionKSubsets(self, nums, k):
        if k == 1:
            return True
        if not nums or len(nums) < k:
            return False
        s = sum(nums)
        # must be divisible by k
        if s % k != 0: return False
        target = s / k
        #print(target)
        nums.sort(reverse=True)
        #print(nums)
        if nums[0] > target:
            return False
        visited = set()
        def partition(k, index, currsum):
            if k == 1:
                return True
            if currsum == target:
                return partition(k-1,0,0)
            for i in range(index, len(nums)):
                if i not in visited and nums[i] + currsum <= target:
                    visited.add(i)
                    if partition(k, i+1, currsum+nums[i]):
                        return True
                    visited.remove(i)
            return False
        return partition(k,0,0)
