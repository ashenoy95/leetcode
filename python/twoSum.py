class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash = {}
        for i in range(len(nums)):
            if nums[i] not in hash:
                hash[target-nums[i]] = i
            else:
                return [hash[nums[i]], i]
                
                
