class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #O(nlogn)
        nums_sorted = sorted(nums)
        i = 0
        j = len(nums) - 1
        while i<j:
            if nums_sorted[i]+nums_sorted[j]>target:
                j-=1
            if nums_sorted[i]+nums_sorted[j]<target:
                i+=1
            else:
                return [nums.index(nums_sorted[i]), nums.index(nums_sorted[j])]
       
