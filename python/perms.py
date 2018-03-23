class Solution(object):
    def swap(self, nums, i, left):
        nums[i], nums[left] = nums[left], nums[i]

    def perm(self, nums, left, final):
        if left==len(nums):
            final.append([num for num in nums])
            return 
        for i in range(left, len(nums)):
            self.swap(nums, i, left)
            self.perm(nums, left+1, final)
            self.swap(nums, i, left)
        return final

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.perm(nums, 0, [])