# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def construct(self, start, end, nums):
        if start>end:
            return None
        mid = (start+end)//2
        root = TreeNode(nums[mid])
        root.left = self.construct(start, mid-1, nums)
        root.right = self.construct(mid+1, end, nums)
        return root
    
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.construct(0, len(nums)-1, nums)