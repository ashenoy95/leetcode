class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        """
        #alternate soln.: O(nlogn) for sorting
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
        """
        hash = {}   #O(n) soln.
        for i in range(len(nums)):
            if nums[i] not in hash:
                hash[target-nums[i]] = i
            else:
                return [hash[nums[i]], i]