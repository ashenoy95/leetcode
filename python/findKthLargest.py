# quick select using random partitioning

import random as rand

class Solution(object):
    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]
    
    
    def randomPartition(self, nums, start, end):
        pivot = rand.randint(start, end)
        self.swap(nums, pivot, end)
        return self.partition(nums, start, end)
    
    
    def partition(self, nums, start, end):
        pivot = nums[end]
        i = start - 1
        
        for j in range(start, end):
            if nums[j]<=pivot:
                i += 1
                self.swap(nums, i, j)
        i += 1
        self.swap(nums, i, end)
        return i
    
    
    def quickSort(self, nums, start, end, k):
        if start<=end:
            pivot = self.randomPartition(nums, start, end)

            if pivot==k:
                return nums[pivot]
            elif pivot<k:
                return self.quickSort(nums, pivot+1, end, k)
            else:
                return self.quickSort(nums, start, pivot-1, k)
            
            
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.quickSort(nums, 0, len(nums)-1, len(nums)-k)