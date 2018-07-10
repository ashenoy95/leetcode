# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def validate(self, node, mini, maxi):
        if not node:
            return True
        
        if (mini!=None and node.val<=mini) or (maxi!=None and node.val>=maxi):
            return False
        
        if not self.validate(node.left, mini, node.val) or not self.validate(node.right, node.val, maxi):
            return False
        
        return True
        
        
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.validate(root, None, None)