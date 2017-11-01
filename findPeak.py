class Solution:
    def peak(self, nums, i, j):
        if j==i:
            return i
        if j-i==1:
            return nums.index(max(nums[i], nums[j]))
        m = int((i+j)/2)
        if nums[m]>=nums[m-1] and nums[m]>=nums[m+1]:
            return m
        elif nums[m-1]>nums[m]:
            return self.peak(nums, i, m-1)
        elif nums[m+1]>nums[m]:
            return self.peak(nums, m+1, j)
    
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.peak(nums, 0, len(nums)-1)