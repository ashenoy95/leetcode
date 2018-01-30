class Solution(object):
    def binarySearch(self, nums, left, right, target):
        if left>right:
            return False
        mid = (left+right)//2
        if nums[mid]==target:
            return True
        if nums[left]<nums[mid]:
            if target>=nums[left] and target<nums[mid]:
                return self.binarySearch(nums, left, mid, target)
            else:
                return self.binarySearch(nums, mid+1, right, target)
        elif nums[mid]<nums[left]:
            if target>nums[mid] and target<=nums[right]:
                return self.binarySearch(nums, mid+1, right, target)
            else:
                return self.binarySearch(nums, left, mid, target)
        elif nums[mid]==nums[left]:
            if nums[mid]!=nums[right]:
                return self.binarySearch(nums, mid+1, right, target)
            else:
                res = self.binarySearch(nums, left, mid-1, target)
                if not res:
                    res = self.binarySearch(nums, mid+1, right, target)
                return res
    
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return False
        return self.binarySearch(nums, 0, len(nums)-1, target)
    
    
    
