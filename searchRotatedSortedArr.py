class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        for i in range(len(nums)):
            if nums[i]==target:
                return i
            if i+1<len(nums):
                if nums[i]>nums[i+1]:
                    break
        if target<nums[0]:
            for j in range(i+1,len(nums)):
                if nums[j]==target:
                        return j
        for j in range(i+1):
            if nums[j]==target:
                return j
        return -1
