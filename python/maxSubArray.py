class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev = nums[0]
        max_so_far = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i]+prev>nums[i]:
                prev = nums[i]+prev
            else:
                prev = nums[i]
                
            if prev>max_so_far:
                max_so_far = prev
                
        return max_so_far