class Solution(object):
    def perm(self, nums, left, final):
        if left==len(nums):
            final.append(nums[:])
            
        for i in range(left, len(nums)):
            nums[i], nums[left] = nums[left], nums[i]
            self.perm(nums, left+1, final)
            nums[i], nums[left] = nums[left], nums[i]

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        perms = []
        self.perm(nums, 0, perms)
        return perms