class Solution(object):
    def searchLeft(self, nums, target, start, end):
        if start>end:
            return -1
        else:
            mid = (start+end)//2
            if nums[mid]==target:
                temp = self.searchLeft(nums, target, start, mid-1)
                if temp==-1:
                    temp = mid
                return temp
            else:
                return self.searchLeft(nums, target, mid+1, end)
    
    def searchRight(self, nums, target, start, end):
        if start>end:
            return -1
        else:
            mid = (start+end)//2
            if nums[mid]==target:
                temp = self.searchRight(nums, target, mid+1, end)
                if temp==-1:
                    temp = mid
                return temp
            else:
                return self.searchRight(nums, target, start, mid-1)
    
    def search(self, nums, target, start, end):
        if start>end:
            return -1
        else:
            mid = (start+end)//2
            if target>nums[mid]:
                return self.search(nums, target, mid+1, end)
            elif target<nums[mid]:
                return self.search(nums, target, start, mid-1)
            else:
                left = mid
                right = mid
                if mid+1<len(nums):
                    if nums[mid+1]==target:
                        right = self.searchRight(nums, target, mid+1, end)
                if mid-1>=0:
                    if nums[mid-1]==target:
                        left = self.searchLeft(nums, target, start, end-1)
                return [left, right]
        
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        r = self.search(nums, target, 0, len(nums)-1)
        if r==-1:
            r = [-1, -1]
        return r
        