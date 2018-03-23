class Solution(object):
    def binarySearch(self, nums, left, right, target):
        if left>right:
            return -1
        mid = (left+right)//2
        if nums[mid]==target:
            return mid
        if nums[left]<nums[mid]:
            if target>=nums[left] and target<nums[mid]:
                return self.binarySearch(nums, left, mid, target)
            else:
                return self.binarySearch(nums, mid+1, right, target)
        else:
            if target>nums[mid] and target<=nums[right]:
                return self.binarySearch(nums, mid+1, right, target)
            else:
                return self.binarySearch(nums, left, mid, target)
    
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        return self.binarySearch(nums, 0, len(nums)-1, target)
